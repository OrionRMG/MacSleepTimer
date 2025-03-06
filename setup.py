from setuptools import setup

APP = ['sleep_timer.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PyQt5'],
    'plist': {
        'CFBundleName': 'MacSleepTimer',
        'CFBundleDisplayName': 'Mac Sleep Timer',
        'CFBundleGetInfoString': 'Provides a simple GUI for setting a sleep timer for your computer, X minutes into the future.',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0'
    },
    'iconfile': 'icons/moon-stars.icns'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

