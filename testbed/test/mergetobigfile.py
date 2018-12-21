import os, sys

print("111")

readsize = 1024

#将指定的formdir下所有文件合并成tofile文件
def join(fromdir, tofile):
    output=open(tofile,"wb")
    #out = open(tofile, "wb")
    parts=os.listdir(fromdir)
    parts.sort()
    for filename in parts: 
        filepath=os.path.join(fromdir,filename)
        fileobj=open(filepath,"rb")
        while True: 
            filebytes=fileobj.read(readsize)
            if not filebytes: 
                break
            output.write(filebytes)
        fileobj.close()
    output.close()

print(222)
join("./folder/", "newfile.ts")
print('333')
