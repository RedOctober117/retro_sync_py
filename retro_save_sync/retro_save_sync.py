from ftplib import FTP

HOST = '192.168.1.216'
PORT = 5000

SAVEFILE_DIRECTORY = '/games/GBA'
SAVE_FOLDER = 'saves/'
SAVE_FILE_NAME = 'Pokemon Unbound v2.1.1.1.sav'
SS0_FILE_NAME = 'Pokemon Unbound v2.1.1.1.ss0'

save = open(SAVE_FOLDER + SAVE_FILE_NAME, 'rb')
ss0 = open(SAVE_FOLDER + SS0_FILE_NAME, 'rb')


dir_contents = None

ftp = FTP()
ftp.connect(HOST, PORT)
with ftp as ftp:
    ftp.login()

    ftp.cwd(SAVEFILE_DIRECTORY)

    ftp.delete(SAVE_FILE_NAME)
    ftp.delete(SS0_FILE_NAME)

    ftp.storbinary('STOR ' + SAVE_FILE_NAME, save)
    ftp.storbinary('STOR ' + SS0_FILE_NAME, ss0)

    # Fact reference: https://datatracker.ietf.org/doc/html/rfc3659.html#section-7.5
    dir_contents = dict(ftp.mlsd(facts=['modify']))

if SAVE_FILE_NAME in dir_contents:
    print(dir_contents[SAVE_FILE_NAME])
