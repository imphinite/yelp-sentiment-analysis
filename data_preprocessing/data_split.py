import os

# Open the large JSON file
with open('../data/yelp_academic_dataset_review.json', 'r', encoding='utf-8') as infile:
    # Set the maximum number of lines per chunk
    max_lines_per_chunk = 500000
    
    # Initialize the chunk counter
    chunk_num = 1

    if not os.path.exists('../data/chunks'):
        os.makedirs('../data/chunks')
    
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
        chunk_file = f'../data/chunks/chunk_{chunk_num}.json'
        with open(chunk_file, 'w', encoding='utf-8') as outfile:
            # Write the lines to the chunk file
            outfile.writelines(lines)
        
        # Increment the chunk counter
        chunk_num += 1
