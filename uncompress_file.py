from zipfile import ZipFile

def uncompress_file(ftp_file, path="", temp_folder="EXTRACT_TEMP"):
    with ZipFile(path+ftp_file, 'r') as zipObj:
        # Extract all the contents of zip file in different directory
        zipObj.extractall(temp_folder)
        print("File "+ftp_file+" uncompressed successfully!")