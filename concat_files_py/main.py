#!/usr/bin/env python3

import os
import sys

def write_file_content(file_path, output_file):
    # Add a JS-style comment with the file name
    output_file.write(f"// FILE NAME: {file_path}\n")
    try:
        # Open and read the file
        with open(file_path, "r", encoding="utf-8") as file:
            contents = file.read()
            # Write to the output file
            output_file.write(contents + "\n\n")
    except UnicodeDecodeError:
        print(f"Warning: Skipping binary file {file_path}")
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")

def process_src_directory(directory_path, output_file):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            write_file_content(file_path, output_file)

def concat_dot_files(directory_path, output_dir=None):
    # Use the provided `output_dir` or default to "~/Documents/flat-files/"
    if output_dir is None:
        output_dir = os.path.expanduser("~/Documents/flat-files/")
    os.makedirs(output_dir, exist_ok=True)

    # Extract the root folder name to use as the output file name
    root_folder_name = os.path.basename(os.path.normpath(directory_path))
    output_file_path = os.path.join(output_dir, f"{root_folder_name}.txt")

    # Open the output file
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        # Process the root directory for dot files
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            if os.path.isfile(item_path) and item.startswith("."):
                write_file_content(item_path, output_file)

        # Recursively process the src directory, if it exists
        src_dir_path = os.path.join(directory_path, "src")
        if os.path.isdir(src_dir_path):
            process_src_directory(src_dir_path, output_file)

    print(f"Concatenated content saved to {output_file_path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: concat-files <directory_path>")
        sys.exit(1)
    directory_path = sys.argv[1]
    concat_dot_files(directory_path)

if __name__ == "__main__":
    main()
