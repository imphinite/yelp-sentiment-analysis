import os

current_dir = os.path.abspath(os.path.dirname(__file__))

parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

data_dir = os.path.join(parent_dir, 'data_preprocessing', 'data')

data_chunks_dir = os.path.join(data_dir, 'chunks')