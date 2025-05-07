# hooks/hook-pyqt6.py
from PyInstaller.utils.hooks import collect_data_files
datas = collect_data_files("PyQt6")