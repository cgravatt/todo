# TODO
<hr>

## Example
```bash
$ todo -h
usage: todo [-h] [-a <name>] [-c <int>] [-p]

Todo Application

options:
  -h, --help            show this help message and exit
  -a <name>, --add <name>
                        Add a new todo item
  -c <int>, --complete <int>
                        Complete a todo item by index
  -p, --print-completed
                        Print completed list
```

```bash
# Create a todo item
$ todo -a "I need to do this"

Todo
========================
0) I need to do this

# Complete a todo item
$ todo -c 0

Todo
========================
```

## Setup
1. Make sure you have python3 install
    ```bash
    sudo apt install python3
    ```
2. Clone the repository to your local workstation
3. Install the file and grant execute
    ```bash
    cp todo.py /usr/local/bin/todo && chmod +x /usr/local/bin/todo
    ```
4. Add your first todo
    ```bash
    todo -a "I need to do this"
    ```