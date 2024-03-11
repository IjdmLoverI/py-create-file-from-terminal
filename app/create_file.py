import argparse
import os
from datetime import datetime


def create_file(directory: str, filename: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = []
    if os.path.exists(os.path.join(directory, filename)):
        with open(os.path.join(directory, filename), "r") as file:
            content = file.readline()
    else:
        content.append(timestamp + "\n")

    line_number = len(content) - 1

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        line_number += 1
        content.append(f"{line_number} {line}")

    with open(os.path.join(directory, filename), "w") as file:
        file.writelines(content)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create or append content to a file")
    parser.add_argument("-d", "--directory", nargs="+",
                        help="Directories to search for or create the file")
    parser.add_argument("-f", "--filename",
                        help="Name of the file to create or append content to")
    args = parser.parse_args()

    if args.directory:
        for directory in args.directory:
            if args.filename:
                create_file(directory, args.filename)


if __name__ == "__main__":
    main()
