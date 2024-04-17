import os
from PIL import Image

def find_file_by_suffix(directory, filename_suffix):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(filename_suffix):
                return os.path.join(root, filename)
    return None

def find_full_paths(txt_loc):
    data_dirs = os.listdir("../color/")
    final_paths = []
    with open(txt_loc, 'r') as infile:
        lines = [line.strip() for line in infile.readlines()]

    for line in lines:
        parts = line.split()
        filename_suffix = f'{parts[0]} {parts[1]}'
        file_location = f'color/{data_dirs[int(parts[2]) - 1]}/'
        full_path = find_file_by_suffix(file_location, filename_suffix)
        final_paths.append(full_path)
    return final_paths

def load_images(final_paths):
    images = []
    for path in final_paths:
        image = Image.open(path)
        #image = np.array(image) / 255.0
        images.append(image)
    return images