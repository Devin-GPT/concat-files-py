# concat-files-py

`concat-files-py` is a Python utility designed to simplify the process of concatenating the contents of `.dot` files and all files within a `src` directory into a single text file. This tool is particularly useful for developers and system administrators who require a quick and efficient method to consolidate file contents for documentation, backup, or archival purposes.

## Features

- Easy concatenation of `.dot` files and source files within a specified directory.
- Recursively processes all files in the `src` directory.
- Outputs a single text file with all contents neatly organized.
- Handles binary file exceptions gracefully.
- CLI support for ease of use directly from the terminal.

## Installation

To install `concat-files-py`, ensure you have Python 3.6 or higher installed on your system. Then, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/concat-files-py.git
   cd concat-files-py
   ```
   
2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
   
3. Install the package:
   ```bash
   python setup.py install
   ```

## Usage

After installation, you can run `concat-files-py` using the following command:
```bash
concat-files <directory_path>
```
Where `<directory_path>` is the path to the directory containing the `.dot` files and the `src` directory you wish to process.

### Example

To concatenate files in the directory `/home/user/projects/my_project`, run:
```bash
concat-files /home/user/projects/my_project
```
This will create a text file in `~/Documents/flat-files/` named after the root directory, containing the concatenated contents of all `.dot` files and files within the `src` directory.

## Contributing

We welcome contributions to `concat-files-py`! If you have suggestions or bug reports, please open an issue in the GitHub repository. If you'd like to contribute code, please submit a pull request:

- Fork the repository.
- Create a new branch for your feature (`git checkout -b feature/amazing-feature`).
- Commit your changes (`git commit -am 'Add some amazing feature'`).
- Push to the branch (`git push origin feature/amazing-feature`).
- Open a pull request.
