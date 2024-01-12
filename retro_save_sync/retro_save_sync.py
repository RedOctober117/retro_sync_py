from ftplib import FTP
from pathlib import Path


HOST = '192.168.1.216'
PORT = 5000

SAVEFILE_DIRECTORY = '/games/GBA'
SAVE_FOLDER = 'saves/'
SAVE_FILE_NAME = 'Pokemon Unbound v2.1.1.1.sav'
SS0_FILE_NAME = 'Pokemon Unbound v2.1.1.1.ss0'
print(Path.cwd())

save = open(SAVE_FOLDER + SAVE_FILE_NAME, 'rb')
ss0 = open(SAVE_FOLDER + SS0_FILE_NAME, 'rb')



ftp = FTP()
ftp.connect(HOST, PORT)
with ftp as ftp:
    ftp.login()
    ftp.cwd(SAVEFILE_DIRECTORY)
    ftp.delete(SAVE_FILE_NAME)
    ftp.delete(SS0_FILE_NAME)
    ftp.storbinary('STOR ' + SAVE_FILE_NAME, save)
    ftp.storbinary('STOR ' + SS0_FILE_NAME, ss0)
    # ftp.transfercmd('put ' + SAVE_FILE_NAME)
    # ftp.transfercmd('put ' + SS0_FILE_NAME)
    ftp.dir()
