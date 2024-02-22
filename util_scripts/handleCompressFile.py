import tarfile,zipfile
import os
def compress_file(tarfilename,dirname):
    if os.path.isfile(dirname):
        with tarfile.open(tarfilename, 'w') as tar:
            tar.add(dirname)
    else:
        with tarfile.open(tarfilename, 'w') as tar:
            for root,dirs,files in os.walk(dirname):
                os.chdir(dirname)
                os.chdir('..')
                path = os.getcwd()
                root_path = os.path.relpath(root,path )
                print("当前文件:",root_path)
                for file in files:
                    file_path=os.path.join(root,file)
                    tar.add(file_path,arcname=os.path.join(root_path,file))

    tar.close()
if __name__=='__main__':
    pass
