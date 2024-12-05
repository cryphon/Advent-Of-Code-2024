import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'elfs')))
import elfs


# paths
inputs = './data'
days = './days'
template = './elfs/template.py'

def create_day(n):
    input_file_path = os.path.join('data', f"day{n}.txt")
    days_file_path = os.path.join('days', f"day{n}.py")
    template_path = os.path.join('elfs', 'template.py')

    # Create directories
    os.makedirs('data', exist_ok=True)
    os.makedirs('days', exist_ok=True)

    # Create empty input file
    with open(input_file_path, 'w') as f:
        f.write("")
    
    # Read and write template
    with open(template_path, 'r') as f:
        template_content = f.read()
    
    with open(days_file_path, 'w') as f:
        f.write(template_content)
def run_day(day_number):
    day_file = os.path.join('days', f"day{day_number}.py")
    if not os.path.exists(day_file):
        print(f"Day {day_number} not found.")
        return
    
    globals_dict = {
        'elfs': elfs,
        'sys': sys,
        '__file__': day_file
    }
    
    with open(day_file, "r") as file:
        exec(file.read(), globals_dict)
if __name__ == "__main__":
    # check if command was given
    if len(sys.argv) < 3:
       print("Provide a command and day number")
       sys.exit()

    # get cmd and day number
    cmd = sys.argv[1]
    day = sys.argv[2]

    # exec cmd
    if cmd == "create":
       create_day(day)
    elif cmd == "run":
       run_day(day)

