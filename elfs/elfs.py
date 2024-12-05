import os

def read_data(path=None):
    if path is None:
        day = get_day(__file__)
        path = os.path.join('data', f'day{day}.txt')
    elif not path.startswith('data/'):
        path = os.path.join('data', f'day{path}.txt')
    with open(path, "r") as file:
        return file.read()

def create_file(path, content=None):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as file:
        file.write(content if content else "")

def get_day(path):
    filename = os.path.basename(path)
    return filename.split('.')[0].replace('day', '')

def read_input(day, split=True):
    path = os.path.join('data', f'day{day}.txt')
    input_data = read_data(path)
    return input_data.splitlines() if split else input_data
