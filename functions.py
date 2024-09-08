FILEPATH = "data.txt"


def get_todos(file_path=FILEPATH):
    """Read a Text file amd return the items as a list"""
    with open(file_path, "r") as file:
        local_todos = file.readlines()
    return local_todos


def write_todos(text, file_path=FILEPATH):
    with open(file_path, "w") as file:
        file.writelines(text)


def add_todo(text, file_path=FILEPATH):
    with open(file_path,'a') as file:
        file.writelines(text)


if __name__ == "__main__":
    print("Testing")