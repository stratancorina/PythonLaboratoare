import os


def find_extensions(path):
    extensions = []
    for (root, directories, files) in os.walk(path):
        for fileName in files:
            full_fileName, ext = os.path.splitext(fileName)
            extensions.append(ext)
    return sorted(extensions)


if __name__ == '__main__':
    path = ".\exemple"
    print(find_extensions(path))
