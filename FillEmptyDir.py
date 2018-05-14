import os

def AddGitEmptyFile(curdir):
    dirfile=os.path.join(curdir,'git.empty')
    f = open(dirfile, 'w')
    f.close()
    return
def Isskipfolder(curdir):
    parentfilelist = os.listdir(os.path.dirname(curdir))
    for file in parentfilelist:
        if file == '.svn':
            havesvn = True;
    if ((curdir == os.path.dirname(curdir) + r'\branches') or 
		(curdir == os.path.dirname(curdir) + r'\tags') or 
		(curdir == os.path.dirname(curdir) + r'\.svn')):
        if havesvn:
            return True
    return False

def fillEmptyDir(curdir):
    dirfiles=os.listdir(curdir)
    #print(len(dirfiles))
    if not dirfiles and not Isskipfolder(curdir) :
        print(r'CREATE git.empty file: '+curdir+r'\git.empty')
        AddGitEmptyFile(curdir)
        return
    else:
        if(os.path.exists(os.path.join(curdir, 'git.empty')) and len(dirfiles)>1 ):
            os.remove(os.path.join(curdir, 'git.empty'))
            print(r'REMOVE git.empty file:'+curdir+r'\git.empty')

    for i in range(0, len(dirfiles)):
        subdir = os.path.join(curdir, dirfiles[i])
        if os.path.isdir(subdir):
            fillEmptyDir(subdir)
    return

fillEmptyDir(os.getcwd())
input("\nPress the ENTER key to exit.")

