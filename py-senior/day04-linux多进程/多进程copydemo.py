import multiprocessing
# from multiprocessing import Pool
import os

# TODO 这段多进程复制文件有问题，后期更改

def copyTask(name,oldFolderName,newFolderName):
    print(name)
    fr = open(oldFolderName+"/"+name)
    fw = open(newFolderName+"/"+name,"w")
    print()
    content = fr.read()
    fw.write(content)

    fw.close()
    fr.close()

def main():
    multiprocessing.freeze_support()
    oldFolderName = "source"

    newFolderName = oldFolderName +"-复件"

    os.mkdir(newFolderName)

    fileNames = os.listdir(oldFolderName)
    pool = multiprocessing.Pool(5)

    for name in fileNames:
        pool.apply_async(copyTask,args=(name,oldFolderName,newFolderName))

    pool.close()
    pool.join()

if __name__ == '__main__':
    main()
