import os


def clean_up(path, directory):
    for file in os.listdir(path):
        os.remove(os.path.join(path, file))
    os.rmdir(directory)
