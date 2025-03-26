# PortableFolderLauncher

A simple Python GUI tool to generate portable batch (.bat) files that open a folder with a relative path. Perfect for USB drives or external devices that may have different drive letters on different computers.

## Features
- Select a source folder you want to launch.
- Select a target folder where the generated `.bat` file will be saved.
- Generates a batch file that will always open the source folder relative to the batch file's location — no matter what drive letter is assigned.
- User-friendly Tkinter-based interface.

## Screenshot
![screenshot](https://github.com/hsuehyt/PortableFolderLauncher/blob/main/images/screenshot.png)

## How It Works
The tool creates a `.bat` file with the following logic:
```bat
@echo off
set "source_folder=%~dp0<relative-path-to-source-folder>"
start "" "%source_folder%"
```
This allows the batch file to always open the source folder correctly from wherever it’s launched.

## Requirements
- Python 3.x
- Tkinter (usually included with Python installations)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/hsuehyt/PortableFolderLauncher.git
```
2. Run the Python script:
```bash
python portable-folder-launcher.py
```

## Usage
1. Select the **Source Folder** — this is the folder you want the batch file to open.
2. Select the **Target Folder** — this is where the batch file will be saved.
3. Click **Generate**.
4. The `.bat` file will be created in your target folder and can be used on any machine.

## License
MIT License.

## Author
[hsuehyt](https://github.com/hsuehyt)
