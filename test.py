
from pathlib import Path, PurePath, PurePosixPath, PureWindowsPath
import os

print('File: ', __file__)
print('Dir: ', os.path.dirname(__file__))
print('AbsPath: ', os.path.abspath(__file__))
print(os.path.join(os.path.dirname('/opt/'), __file__))
print(os.path.abspath(os.path.dirname(__file__)))
print(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'hector.txt'))
print('Using PurePosixPath: ', PurePosixPath(Path.cwd()).joinpath('hector.txt'))

print('Using PathLib.Path: ', Path(__file__))
print('Using PurePosixPath: ', PurePosixPath(Path.cwd()).joinpath(__file__))
print(PurePath(__file__))
print(PurePosixPath(__file__))
print(PureWindowsPath(__file__))

print('__name__ ', __name__)
print('__package__ ', __package__)