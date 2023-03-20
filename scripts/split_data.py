import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import paths
from data_preprocessing.split_data import split_data
# from utils.db_connection import conn




if __name__ == '__main__':
    split_data()
