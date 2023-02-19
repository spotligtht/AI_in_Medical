import os
from pypinyin import pinyin, lazy_pinyin
# 将病例文件中文名改成拼音
# 一层文件
def rename():
    path = r"E:\Prostate-JD2-BPH"
    filelist = os.listdir(path)  # 该文件夹下所有的文件（包括文件夹）
    for files in filelist:  # 遍历所有文件
        Olddir = os.path.join(path, files)  # 原来的文件路径
        filename = os.path.splitext(files)[0] # 获取文件名
        # 把文件名里的汉字转换成其首字母
        filename1 = lazy_pinyin(filename)  # , style=pypinyin.FIRST_LETTER
        # 创建一个空列表
        filename2 = []
        for ch in filename1:
            filename2.extend(ch)
        # 把列表转换成没有间隔的字符串，因为文件名要以字符串形式存在
        filenameToStr = ''.join(filename2)
        filetype = os.path.splitext(files)[1] # 文件扩展名
        Newdir = os.path.join(path, filenameToStr + filetype)  # 新的文件名
        os.rename(Olddir, Newdir)  # 重命名
rename()
