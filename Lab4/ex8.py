import os


def get_files_path(dir_path):
    files = os.listdir(dir_path)
    files_path = []
    for file in files:
        files_path.append(os.path.join(dir_path, file))
    return files_path


if __name__ == '__main__':
    print(get_files_path("E:\AN3\python\lab4"))