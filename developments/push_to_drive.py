import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


gauth = GoogleAuth()
gauth.LocalWebserverAuth()

def upload_file(path):
    try:
        drive = GoogleDrive()

        file_name = path.split('/')[-1]

        file = drive.CreateFile(file_name)
        file.SetContentFile(os.path.join(path, file_name))
        file.Upload()

        return f'File {file_name} was uploaded!'
    except Exception as ex:
        return 'Got some trouble...'

def main():
    print(upload_file(path='/Users/yarik/PycharmProjects/ProjOnConda/developments/weight_calc.py'))

if __name__ == '__main__':
    main()