import PyInstaller.__main__
import os
import sys
import subprocess
import platform

def build_executable(script_path, icon_path=None, additional_files=None, name=None, command=None):

    """Builds a Python executable using PyInstaller.

    Args:
        script_path (str): Path to the main Python script.
        icon_path (str, optional): Path to the icon file (.ico). Defaults to None.
        additional_files (list, optional): List of tuples, where each tuple contains
            (source, destination) for additional files to include. Defaults to None.
        name (str, optional): The name for the executable. If None, the script name is used.
    """

    command = [script_path]

    if name:
        command.extend(["--name", name])

    if icon_path:
        command.extend([f'--icon={icon_path}'])

    if additional_files:
      for source, destination in additional_files:
        command.extend(["--add-data", f"{source};{destination}"])  # Correct format for --add-data

    # Important PyInstaller Options for cleaner builds
    command.extend(["--onefile"])  # Creates a single executable file
    command.extend(["--noconsole"]) # Prevents the console window from appearing (for GUI apps)
    command.extend(["--clean"])  # Cleans the build directory before building

    # Add any other PyInstaller flags here as needed, e.g.,
    # --windowed for GUI apps (same as --noconsole)
    # --add-binary for including DLLs or other binaries

    try:
        PyInstaller.__main__.run(command)
        print(f"Executable built successfully for {script_path}")
    except Exception as e:
        print(f"Error building executable: {e}")


if __name__ == "__main__":
    script_path = "calculator/main.py"  # Replace with your script's path
    icon_path = "icon.ico"  # Replace with your icon's path or None
    #additional_files = [
       # ("path/to/data_file.txt", "."),  # Example: Include data_file.txt in the same directory as the exe
        #("path/to/images", "images"),      # Example: Include the images directory
    #]

    build_executable(script_path, icon_path, name="CalculatorApp") # Name the executable

    # Example without icon and additional files
    # build_executable("my_script.py")