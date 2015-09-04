import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'
    
options = {
    'build_exe': {
        'includes': 'atexit' 
    }
}

executables = [ Executable(
    'UnitConverter.py',
    base=base,
    shortcutName='Unit Converter',
    shortcutDir='DesktopFolder'
    )]

setup(  
        name = "Unit Converter",
        version = "1.0",
        description = "Converts length, volume and weight units",
        executables = executables,
        options = options
      )