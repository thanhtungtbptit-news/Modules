f= open("README","r",encoding="utf-8")
file = f.read()
print(file)
f.close()

f=open("README","r",encoding="utf-8")
for line in f:
    print(line.strip())
f.close()

f=open("README","r",encoding="utf-8")
print(f.readline())
print(f.readlines())
f.close()

f=open("file.txt","w",encoding="utf-8")
f.write("Xin chào Python \n")
f.write("Học lập trình thật vui vẻ \n ")
f.close()

f=open("file.txt","a",encoding="utf-8")
f.write("Thêm dòng mới ko chèn lên ")
f.close()