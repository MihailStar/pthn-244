import os

text = input()


def write_and_read(text: str) -> str:
    file_path = os.path.join(os.path.abspath("/tmp"), "my_file")

    with open(file_path, "w") as file:
        file.write(text)

    with open(file_path, "r") as file:
        return file.read()


print(write_and_read(text))
