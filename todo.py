#!/usr/bin/env python3
import argparse
import os


def base_dir():
    return os.environ['HOME'] + '/.todo'


def todo_file():
    return base_dir() + '/todo.txt'


def completed_file():
    return base_dir() + '/done.txt'


def complete(indices_to_complete):

    completed_lines = []
    with open(todo_file(), 'r') as tfile:
        lines = tfile.readlines()
        for i in indices_to_complete:
            completed_lines.append(lines[i])
            del lines[i]

    with open(todo_file(), 'w') as tfile:
        tfile.writelines(lines)

    with open(completed_file(), 'a') as cfile:
        for cline in completed_lines:
            cfile.write(cline + '\n')

    print_todo()


def add(items_to_add):
    os.makedirs(base_dir(), exist_ok=True)

    with open(todo_file(), 'r') as f:
        lines = f.readlines()
        for idx, item in enumerate(items_to_add):
            if item + '\n' in lines:
                del items_to_add[idx]

    with open(todo_file(), 'a') as f:
        for item in items_to_add:
            f.write(item + '\n')

    print_todo()


def print_todo():
    print("Todo")
    print("========================")
    with open(todo_file(), 'r') as f:
        for idx, line in enumerate(f.readlines()):
            print(str(idx) + ') ' + line.strip())


def main():
    parser = argparse.ArgumentParser(prog="todo", description="Todo Application")
    parser.add_argument('-a', '--add', action="append", dest="add_items", metavar="<name>", help='Add a new todo item')
    parser.add_argument('-c', '--complete', action="append", dest="complete_items", metavar="<int>", type=int, help="Complete a todo item by index")

    args = parser.parse_args()

    if args.add_items is not None:
        add(args.add_items)
    elif args.complete_items is not None:
        complete(args.complete_items)
    else:
        print_todo()

if __name__ == '__main__':
    main()
