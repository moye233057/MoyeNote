import os
import sys
import stat
import time
import shutil


# 查看文件的具体数据
def watchfiledata(filepath):
    try:
        with open(filepath) as f:
            linecount = (sum(1 for line in f))
            f.seek(0)
            charcount = (sum([len(line) for line in f]))
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

    file_name = filepath.split('/')[-1]
    file_stats = os.stat(filepath)
    # create a dictionary to hold file info
    file_info = {
        '文件名': file_name,
        '文件大小': file_stats[stat.ST_SIZE],
        '上一次更改时间': time.strftime("%Y/%m/%d %I:%M:%S %p",
                                 time.localtime(file_stats[stat.ST_MTIME])),
        '上一次访问时间': time.strftime("%Y/%m/%d %I:%M:%S %p",
                                 time.localtime(file_stats[stat.ST_ATIME])),
        '创建时间': time.strftime("%Y/%m/%d %I:%M:%S %p",
                              time.localtime(file_stats[stat.ST_CTIME])),
        '行数': linecount,
        '字数': charcount,
    }
    for k, v in file_info.items():
        print(k, v)


# 计算目录下面文件的总大小
def folder_size(path):
    dir_size = 0
    fsizedicr = {'Bytes': 1,
                 'Kilobytes': float(1) / 1024,
                 'Megabytes': float(1) / (1024 * 1024),
                 'Gigabytes': float(1) / (1024 * 1024 * 1024)}
    for (path, dirs, files) in os.walk(path):
        for file in files:
            filename = os.path.join(path, file)
            dir_size += os.path.getsize(filename)

    fsizeList = [str(round(fsizedicr[key] * dir_size, 2)) + " " + key for key in fsizedicr]

    if dir_size == 0:
        print("File Empty")
    else:
        # 反向排序列表，将最小单位的大小优先打印.
        for units in sorted(fsizeList)[::-1]:
            print("Folder Size: " + units)


# 批量重命名指定目录下面所有文件的后缀名
def batch_rename(work_dir, old_ext, new_ext):
    """
    Args:
        work_dir: 需要修改扩展名的文件的上级目录.str
        old_ext: 旧扩展名.str
        new_ext: 新扩展名.str
    Returns:None
    """
    # files = os.listdir(work_dir)
    for filename in os.listdir(work_dir):
        # 获取扩展名
        # splitext能分离文件名和扩展名
        split_file = os.path.splitext(filename)
        # 分离元祖元素
        root_name, file_ext = split_file
        # 检查该文件扩展名是否是需要修改的扩展名
        if old_ext == file_ext:
            # 设置包含新扩展名的文件的名称
            newfile = root_name + new_ext
            # 重命名
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )
    print("rename is done!")
    print(os.listdir(work_dir))


# 移动一个目录下指定天数的文件到另一个目录下
def MoveFilesToOtherFolder(src, des, days):
    now = time.time()
    for f in os.listdir(src):  # Loop through all the files in the source directory
        fpath = src + '/' + f
        if os.stat(fpath).st_mtime > now - days * 86400:
            if os.path.isfile(fpath):
                shutil.move(fpath, des)
        else:
            print('不符合')


# 获取一个目录下指定扩展名的文件
def GetSameExtFiles(path):
    files = [pos_json for pos_json in os.listdir(path) if pos_json.endswith('.json')]
    return files


if __name__ == '__main__':
    # work_dir = './test'
    # old_ext = '.txt'
    # new_ext = '.png'
    # batch_rename(work_dir, old_ext, new_ext)
    # print('_________________________________')
    # path = './test/1.png'
    # watchfiledata(path)
    # print('_________________________________')
    # path = './pandas'
    # folder_size(path)
    # print('_________________________________')
    # src = './test'
    # des = './pandas'
    # days = 30
    # sf = os.listdir(src)
    # print(sf)
    # for f in sf:
    #     t = os.stat(src + '/' + f).st_mtime
    #     print(t)
    # MoveFilesToOtherFolder(src, des, days)
    print('_________________________________')
