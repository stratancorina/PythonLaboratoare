import os


def function2(directory: str, file: str):
    with open(file, "w") as fd:
        [fd.write(os.path.abspath(f) + os.linesep) for f in os.listdir(directory) if
         f.startswith("a")]


if __name__ == '__main__':
    function2(".\exemple", ".\exemple\\file.txt")
