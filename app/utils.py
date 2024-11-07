import os
from datetime import date
import pandas as pd
import shutil


datetoday = date.today().strftime("%d-%B-%Y")

# Функция для создания необходимых директорий
def create_directories():
    if not os.path.isdir('app/db'):
        os.makedirs('app/db')
    if not os.path.isdir('app/Attendance'):
        os.makedirs('app/Attendance')
    if not os.path.isdir('app/faces_data'):
        os.makedirs('app/faces_data')
    if not os.path.isdir('app/faces_data/faces'):
        os.makedirs('app/faces_data/faces')
    if f'Attendance-{datetoday}.csv' not in os.listdir('app/Attendance'):
        with open(f'app/Attendance/Attendance-{datetoday}.csv', 'w') as f:
            f.write('Name,Lastname,Time')


# Функция для извлечения информации о посещаемости из файла
def extract_attendance():
    datetoday = date.today().strftime("%d-%B-%Y")
    df = pd.read_csv(f'app/Attendance/Attendance-{datetoday}.csv', encoding='utf-8')  
    names = df['Name']
    lastnames = df['Lastname']
    classes = df['Class']
    times = df['Time']
    l = len(df)
    return names, lastnames, classes, times, l


# Функция для очистки каталога faces_data
def clear_userlist():
    faces_data_path = 'app/faces_data'
    if os.path.exists(faces_data_path):
        shutil.rmtree(faces_data_path)  # Удаляет папку и все ее содержимое
        os.makedirs(faces_data_path)  # Создает пустую папку 'faces_data' заново
    else:
        print(f"Папка '{faces_data_path}' не существует.")
