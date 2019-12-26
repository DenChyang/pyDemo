import os, multiprocessing

q = None

def getFilesCount(dirName):
    if dirName == None or not os.path.isdir(dirName):
        return

    files = os.listdir(dirName)
    for item in files:
        absolutePath = dirName + os.sep + item
        if os.path.isdir(absolutePath):
            getFilesCount(absolutePath)
        else:
            if q.full():
                print("缓存已满")
            else:
                q.put(absolutePath)


def copyFile(destination, file, oldDir):
    if destination == None or file == None:
        return
    if (not os.path.isdir(destination)) or (not os.path.exists(file)):
        return

    subDir = file[file.find(oldDir) + len(oldDir) + 1:file.rfind(os.sep)]
    newDir = destination + os.sep + subDir
    if not os.path.exists(newDir):
        os.mkdir(newDir)
    fileName = file[file.rfind(os.sep) + 1:]

    newFileName = newDir + os.sep + fileName
    newFile = open(newFileName, "wb")
    newFile.write(open(file, "rb").read())
    newFile.close()

def main():
    multiprocessing.freeze_support()

    dirName = "source"
    newDirName = "source_copy"
    if not os.path.isdir(dirName):
        print("无此文件夹")
        return
    if os.path.exists(newDirName):
        print("目标文件夹已存在")
        return
    os.mkdir(newDirName)

    global q
    q = multiprocessing.Manager().Queue()
    getFilesCount(dirName)
    pool = multiprocessing.Pool(processes=3)

    while not q.empty():
        pool.apply_async(func=copyFile, args=(newDirName, q.get(), dirName, ))
    pool.close()
    pool.join()

    while not q.empty():
        pass
    print("复制完毕")

if __name__ == "__main__":
    main()