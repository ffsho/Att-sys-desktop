from pathlib import Path
import os


ROOT_PATH = Path(__file__).resolve().parents[1]
DB_FOLDER_PATH = os.path.join(ROOT_PATH, 'app\\db')
DB_PATH = os.path.join(ROOT_PATH, 'app\\db\\Users.db')
ATTENDANCE_FOLDER_PATH = os.path.join(ROOT_PATH, 'app\\Attendance')
FACES_DATA_PATH = os.path.join(ROOT_PATH, 'app\\faces_data')
FACES_IMG_PATH = os.path.join(ROOT_PATH, 'app\\faces_data\\faces')