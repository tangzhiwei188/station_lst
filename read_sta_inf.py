import numpy as np
num_sta=496
def check_charset(file_path):
    import chardet
    with open(file_path,"rb") as f:
        data=f.read(4)
        charset=chardet.detect(data)['encoding']
    return charset
your_path="sanhe_sta_info_new.txt"
with open(your_path,encoding=check_charset(your_path)) as f:
    #data = f.read()
    print("filename:",f.name)
    filelist=f.readlines()#将txt文件转换为所有的行组成的列表
    numberoflines =len(filelist)#得到行数         
    print ("number of lines: %s" % (numberoflines))
    returnMat = np.zeros((numberoflines,4)) #生成一个numberoflines行，3列的矩阵
    classLabelVector =[]
    index=0
    for line in filelist: #依次读取每行
        line=line.strip()  #去掉每行头尾空白
        listline=line.split() #按换行符\n、制表符\t、空字符串''分割数据
        print(listline[0:4])
        returnMat[index,:] =listline[0:4]  #将文本数据前三列存入数据矩阵
        index+=1
    returnMat[:,1:2]=returnMat[:,1:2]-453000000
    #print(returnMat[:,1])  
    #np.savetxt('station.lst',np.c_[returnMat[:,[1]]],fmt='%05d',delimiter = ' ')  
    f=open("station.lst","w")
    for i in range(0,num_sta):
        print('%05d'%returnMat[[i],[1]],file=f,end=' ')
        print('%3.6f'%returnMat[[i],[2]],file=f,end=' ')
        print('%2.6f'%returnMat[[i],[3]],file=f)
    f.close()