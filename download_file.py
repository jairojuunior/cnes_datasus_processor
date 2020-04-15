import shutil
import urllib.request as request
from contextlib import closing

def download_zip(ftp_root, ftp_file,  path=""):

    with closing(request.urlopen(ftp_root+"/"+ftp_file)) as r:
        with open(path+ftp_file, 'wb') as f:
            shutil.copyfileobj(r, f)
        print("File "+ftp_file+" downloaded successfully!")