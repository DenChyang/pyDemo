import os
import multiprocessing

def copyFileTask(name,oldFile,newFile,queue):
    fr = open(oldFile+"/"+name)
    fw = open(newFile+"/"+name,"w")
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
    queue = multiprocessing.Manager().Queue(50)
    for name in fileName:
        pool.apply_async(copyFileTask,args=(name,old_file,new_file,queue))
    # queue.get()
    pool.close()
    pool.join()
if __name__ == '__main__':
    main()

