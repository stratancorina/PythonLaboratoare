import os


def get_file_info(path):
    info = {"full_path": path, "file_size": os.path.getsize(path), "file_extension": os.path.splitext(path)[1],
            "can_read": os.access(path, os.R_OK), "can_write": os.access(path, os.W_OK)}
    return info


if __name__ == '__main__':
    print(get_file_info(".\exemple\\buna-ziua.txt"))