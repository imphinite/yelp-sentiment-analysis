import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import linecache
from tqdm import tqdm
from utils import paths


def split_data(filename='yelp_academic_dataset_review.json', max_lines_per_chunk=500000, output_dir=paths.data_chunks_dir):
    # Open the large JSON file
    filepath = os.path.join(paths.data_dir, filename)

    print('Estimating workload..')
    total_lines = len(linecache.getlines(filepath))

    # Initialize progress bar
    pbar = tqdm(total=total_lines, desc="Split file " + filename)

    # Open file and start splitting
    with open(filepath, 'r', encoding='utf-8') as infile:        
        # Initialize the chunk counter
        chunk_num = 1

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Read the file in chunks and write each chunk to a separate file
        while True:
            # Read the next chunk of lines
            lines = []
            for i in range(max_lines_per_chunk):
                line = infile.readline()
                if not line:
                    break
                lines.append(line)
            
            # If there are no more lines, break out of the loop
            if not lines:
                break

            # Create a new file for the chunk

            chunk_file = os.path.join(paths.data_chunks_dir, f'chunk_{chunk_num}.json')
            # chunk_file = f'./data/chunks/chunk_{chunk_num}.json'
            with open(chunk_file, 'w', encoding='utf-8') as outfile:
                # Write the lines to the chunk file
                outfile.writelines(lines)
            
            # Increment the chunk counter
            chunk_num += 1

            pbar.update(len(lines))


if __name__ == '__main__':
    split_data()
