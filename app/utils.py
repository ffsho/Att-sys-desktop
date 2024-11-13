import os
from datetime import date
import pandas as pd
import shutil
from app.definitions import *


datetoday = date.today().strftime("%d-%B-%Y")

# Функция для создания необходимых директорий
def create_directories():
    if not os.path.isdir(DB_FOLDER_PATH):
        os.makedirs(DB_FOLDER_PATH)
    if not os.path.isdir(ATTENDANCE_FOLDER_PATH):
        os.makedirs(ATTENDANCE_FOLDER_PATH)
    if not os.path.isdir(FACES_DATA_PATH):
        os.makedirs(FACES_DATA_PATH)
    if not os.path.isdir(FACES_IMG_PATH):
        os.makedirs(FACES_IMG_PATH)
    if f'Attendance-{datetoday}.csv' not in os.listdir(ATTENDANCE_FOLDER_PATH):
        with open(os.path.join(ATTENDANCE_FOLDER_PATH, f'Attendance-{datetoday}.csv'), 'w') as f:
            f.write('Name,Lastname,Time')


# Функция для извлечения информации о посещаемости из файла
def extract_attendance():
    datetoday = date.today().strftime("%d-%B-%Y")
    df = pd.read_csv(os.path.join(ATTENDANCE_FOLDER_PATH, f'app/Attendance/Attendance-{datetoday}.csv'), encoding='utf-8')  
    names = df['Name']
    lastnames = df['Lastname']
    classes = df['Class']
    times = df['Time']
    l = len(df)
    return names, lastnames, classes, times, l


# Функция для очистки каталога faces_data
def clear_userlist():
    if os.path.exists(FACES_DATA_PATH):
        shutil.rmtree(FACES_DATA_PATH)  # Удаляет папку и все ее содержимое
        os.makedirs(FACES_DATA_PATH)  # Создает пустую папку 'faces_data' заново
    else:
        print(f"Папка '{FACES_DATA_PATH}' не существует.")
