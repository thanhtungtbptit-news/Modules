with open("file.txt","r",encoding="utf-8") as f :
    for  line in f :
        print(line.strip())

with open("book.txt","w",encoding="utf-8") as file :
    file.write("Hôm nay học Python !\n")
    file.write("Thực hành phần File. \n")        

with open("file.txt","rb") as f :
    data=f.read()
    print("Kích cỡ file: " ,len(data),"bytes")    

with open ("copy.jpg","wb") as f :
    f.write(data)    

students=["Tùng","An","Long","Thành Anh"]
with open("students.txt","w",encoding="utf-8") as f:
    for s in students :
        f.write(s + "\n")   

with open("students.txt","r",encoding="utf-8") as f :
    names=f.readlines()
    for n in names:
        print("Sinh viên : ",n.strip())    
