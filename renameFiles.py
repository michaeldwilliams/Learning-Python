import os

def renameFiles():
    #(1) get file names from a folder
    fileDirectory = os.listdir("/Users/michaeldwilliams/Desktop/prank")
    print(fileDirectory)
    savedPath = os.getcwd()
    print(savedPath)
    os.chdir("/Users/michaeldwilliams/Desktop/prank")
    #(2) for each file, rename filename
    for fileName in fileDirectory:
        print "Old file name: ",fileName
        print "New file name: ",fileName.translate(None, "0123456789")
        os.rename(fileName, fileName.translate(None, "0123456789"))
renameFiles()
