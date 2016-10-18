import os
# not sure why this doesnt work at this point


def rename_files():
    # get all file names
    file_list = os.listdir(r"C:\Users\212329582\Documents\Udacity\FoundationsPython\lesson1\photos\prank")

    saved_path = os.getcwd()
    os.chdir(r"C:\Users\212329582\Documents\Udacity\FoundationsPython\lesson1\photos\prank")

    # rename all files without numbers
    for  file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))

    os.chdir(saved_path)

rename_files()