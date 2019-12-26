import os

from multiprocessing import Pool,Manager


def copyFileTask(name,oldFile,newFile,queue):
    """
    文件拷贝的方法
    :param oldFile:
    :param newFile:
    :return:
    """
    print("name:%s"%name)
    fr = open(oldFile+"/"+name)
    fw = open(newFile+"/"+name,"w")
    print("+===========================+")
    # while True:
    #     content = fr.read(1024)
    #     if len(content)==0:
    #         break

    content = fr.read()

    fw.write(content)
    fr.close()
    fw.close()
    queue.put(name)

def main():
    """
    主函数
    :return:
    """
    # 获取文件夹的名字
    #old_file = input("file")
    old_file = "../source"

    # 1.创建一个文件夹
    new_file = old_file + "[copy]"
    os.mkdir(new_file)

    # 2.获取old文件夹中所有的文件
    fileName = os.listdir(old_file)

    # 3.使用多进程进行copy文件
    pool= Pool(5)
    queue = Manager().Queue()
    for name in fileName:
        pool.apply_async(copyFileTask,args=(name,old_file,new_file,queue))

    pool.close()
    pool.join()

    # 用队列显示拷贝进度
    num = 0
    allCount = len(fileName)
    while num < allCount:
        queue.get()
        num+= 1
        print()
        print("num=%d"%num)
        copyRate = (num / allCount)
    #     print("\r拷贝文件的进度:%.2f%%"%(copyRate*100),end="")
        # if :
        #     break

if __name__ == '__main__':
    main()

