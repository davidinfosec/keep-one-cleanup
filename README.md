# Keep-One-Cleanup

## Overview

`k1cleanup.py` is a Python script designed to clean up directories by removing all files except one specified file. This script is useful when you want to retain a specific file and delete everything else within a directory.

Example: I have 20 folders, all which contain KJV.json, and I want to delete everything from all 20 folders, except KJV.json:

![firefox_AIL91gisYe](https://github.com/davidinfosec/keep-one-cleanup/assets/87215831/0db8bfb8-514d-4cbe-99a4-e0dc5d3941ec)

## Usage

1. **Download the Script**: Download `k1cleanup.py` to your local machine.

2. **Open the Script**: Open `k1cleanup.py` in a text editor.

3. **Specify Parameters**: Edit the script and specify the following parameters (at the bottom of the script):
   - `root_dir`: The root directory you want to clean up.
   - `keep_file`: The name of the file you want to keep.

   ```python
   # Define the root directory and the file you want to keep
   root_dir = "/path/to/your/root/directory"
   keep_file = "file_to_keep.txt"
   ```

4. **Run the Script**: Execute the script using Python.

   ```
   python k1cleanup.py
   ```

You can also use my tool, Task Runway, to run it easily.
https://taskrunway.com
![firefox_1spHK2N83C](https://github.com/davidinfosec/keep-one-cleanup/assets/87215831/11542805-3d96-49d7-9650-9a6d6cccbe96)


## Important Notes

- Ensure that you specify the correct `root_dir` and `keep_file` before running the script.
- The script will delete all files within the specified `root_dir`, except for the one specified in `keep_file`.
- Use with caution, as it can permanently delete files within the directory.

## Contributing

If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Feel free to adjust the content as needed for your specific script.
