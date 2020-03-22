#coding:utf-8

import os,sys,platform

def eachFile(filepath):   #获取目录下所有文件的名称
    pathDir = os.listdir(filepath)
    list=[]
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        fileName=child.replace(filepath,'')
        list.append(fileName)
    return list

def getPath():
	filePath = 'F:/照片&视频/Canon/' + input(
		'F:/照片&视频/Canon/'
		)
	return filePath

def checkFiles(filepath):
	file_list = eachFile(filepath)
	name_to_remove = []
	for f in file_list:
		if 'MP4' in f:
			name_to_remove.append(f)
		elif 'JPG' in f:
			name_to_remove.append(f)
			name_to_remove.append(f[:-4]+'.CR2')
	for i in name_to_remove:
		file_list.remove(i)
	return file_list

def del_file(path):     #递归删除目录及其子目录下的文件
    for i in os.listdir(path):
        path_file = os.path.join(path, i) #取文件绝对路径
        if os.path.isfile(path_file):     #判断是否是文件
            os.remove(path_file)
        else:
            del_file(path_file)

def remove_file(path,file_list):
    for filename in file_list:
        if(os.path.exists(path+filename)):   #判断文件是否存在
            if(os.path.isdir(path+filename)):
                del_file(path+filename)
            else:
                if(os.path.exists(path+filename)):
                    os.remove(path+filename)
        else:
            print(path+filename+' is not exist!')

if __name__ == '__main__':
	filePath = getPath()
	delete_list = checkFiles(filePath)
	remove_file(filePath+'/',delete_list)
