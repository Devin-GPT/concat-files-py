import tempfile
import os
from concat_files_py.main import concat_dot_files  # Adjust the import path as needed

def test_concat_dot_files():
    with tempfile.TemporaryDirectory() as tempdir:
        os.makedirs(f"{tempdir}/src", exist_ok=True)
        dot_file_path = os.path.join(tempdir, ".example")
        src_file_path = os.path.join(tempdir, "src/example.txt")

        with open(dot_file_path, "w") as f:
            f.write("Dot file content\n")
        with open(src_file_path, "w") as f:
            f.write("Src file content\n")

        expected_output = "// FILE NAME: " + dot_file_path + "\nDot file content\n\n\n" + \
                          "// FILE NAME: " + src_file_path + "\nSrc file content\n\n\n" 

        output_dir = os.path.join(tempdir, "output")
        concat_dot_files(directory_path=tempdir, output_dir=output_dir)  # Ensure this matches your script's function signature

        output_file_path = os.path.join(output_dir, os.path.basename(os.path.normpath(tempdir)) + ".txt")
        with open(output_file_path, "r") as f:
            output = f.read()
            
            print("=== Expected Output ===")
            print(repr(expected_output))
            print("=== Actual Output ===")
            print(repr(output))
            assert output == expected_output, "Output file did not match expected content"