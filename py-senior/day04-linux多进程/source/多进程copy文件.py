import os
import multiprocessing

def copyFileTask(name,oldFile,newFile,queue):
    fr = open(oldFile+"/"+name,encoding="utf-8")
    fw = open(newFile+"/"+name,"w",encoding="utf-8")
    content = fr.read()
    fw.write(content)
    fr.close()
    fw.close()
    print("+===========================+")
    print("name:%s"%name)
    queue.put(name)
    print("队列长度%d"%queue.qsize())

def main():
    multiprocessing.freeze_support()
    # 获取文件夹的名字
    #old_file = input("file")
    old_file = "../source"
    # 1.创建一个文件夹
    new_file = old_file + "[copy]"
    os.mkdir(new_file)
    # 2.获取old文件夹中所有的文件
    fileName = os.listdir(old_file)
    # 3.使用多进程进行copy文件
    pool= multiprocessing.Pool(5)
    queue = multiprocessing.Manager().Queue()
    for name in fileName:
        pool.apply_async(copyFileTask,args=(name,old_file,new_file,queue))

    num = 0
    allCount = len(fileName)

    while num < allCount:
        queue.get()
        num+= 1
        copyRate = num/allCount *100
        print("\r 复制文件进度：%.2f %% "%copyRate,end="")

    # pool.close()
    # pool.join()
if __name__ == '__main__':
    main()

