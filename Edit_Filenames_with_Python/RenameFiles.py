import os
def rename_files():
    #find file path
    # get file with 'os.listdir'
    fileDirection = os.listdir("/Users/merongoitom/Desktop/Nanodegree/IntroToPython/Filenames/prank")
    print (fileDirection)
    saved_path = os.getcwd()
    os.chdir("/Users/merongoitom/Desktop/Nanodegree/IntroToPython/Filenames/prank")
    #rename files in path
    for i in fileDirection:
        print ('new name - ' + i)
        print ('old name -' + i.translate(None,'0123456789'))
        os.rename(i, i.translate(None,'0123456789'))
		
    os.chdir(saved_path)
rename_files()