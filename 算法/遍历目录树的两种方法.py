from os import listdir
from os.path import join, isfile, isdir

import os
from collections import deque


path = r"E:\慕课网\Python高级编程和异步IO并发编程(1)"

#广度优先遍历
def BFS_dir(path):
    queue = deque([])  # 队列
    queue.append(path)
    while len(queue) != 0:
        path = queue.popleft()  # 从队列取出值
        filelist = os.listdir(path)  # 遍历路径
        for filename in filelist:
            filepath = os.path.join(path, filename)

            if os.path.isdir(filepath):
                print("文件夹", filename)
                queue.append(filepath)  # 加入队列
            else:
                print("文件", filename)


#深度优先遍历
def DFS_dir(directory):
    for subPath in listdir(directory):
        path = os.path.join(directory, subPath)
        if os.path.isfile(path):
            print(path)
        elif os.path.isdir(path):
            print(path)
            DFS_dir(path)

DFS_dir(path)