# Custom DS RPC

A customizable Discord Rich Presence application written in Python.

## About

Custom DS RPC allows users to customize their Discord activity by changing activity details, state, images, and custom buttons.

The project includes both a console version and a graphical interface built with PySide6.

## Features

- Connects to Discord Rich Presence.
- Customize activity details and state.
- Select large and small images from available Discord assets.
- Customize two Discord activity buttons with your own labels and URLs.
- Save and restore application settings.
- Reset settings to default values.
- Dark-themed graphical interface.

## Technologies

- Python
- PySide6
- pypresence
- JSON
- PyInstaller

## Project Structure

```text
custom_rpc/
├── app/
│   ├── __init__.py
│   └── window.py
├── rpc/
│   ├── __init__.py
│   └── presence.py
├── main.py
├── gui_main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/witchblxvdes/custom_ds_rpc.git
```

2. Navigate to the project directory:

```bash
cd custom_ds_rpc
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Console Version

Run the console application:

```bash
python main.py
```

### GUI Version

Run the graphical application:

```bash
python gui_main.py
```

## Building an Executable

Install PyInstaller:

```bash
pip install pyinstaller
```

Build the GUI application:

```bash
python -m PyInstaller --onefile --windowed --name "Custom DS RPC" gui_main.py
```

The executable will be available in the `dist` directory.

## Settings

Application settings are stored in `settings.json`.

The file is created automatically and contains activity details, state, selected image keys, and custom button settings.

The two Discord activity buttons can be customized directly in the GUI by changing their labels and URLs.

Use the **Reset Settings** button to restore the default configuration.

## License

MIT