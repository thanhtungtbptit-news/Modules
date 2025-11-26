#Bai1
lst = [1, 2, 3, 4, 5]
tong = 0
for x in lst:
    tong += x
print("Tổng =", tong)

#Bai2
lst = ["a", "b", "a", "c", "a"]
chuoi = input("Nhập chuỗi cần đếm trong lst: ")
print("Số lần xuất hiện:", lst.count(chuoi))

#Bai3
lst = [4, 8, 2, 10, 5]
max_val = lst[0]
for i in lst:
    if i > max_val:
        max_val = x
print("Giá trị lớn nhất:", max_val)

#Bai4
t = (1, 3, 5, 7)
x = int(input("Nhập số cần kiểm tra: "))
if x in t:
    print("Có trong tuple")
else:
    print("Không có trong tuple")

#Bai5
lst = [1, 2, 2, 3, 4, 4, 5]
s = set(lst)
print("Set:", s)
print("Số phần tử sau khi loại trùng:", len(s))   

#Bai6
lst = [1, 2, 3, 4]
new_lst = []
for i in range(len(lst)-1, -1, -1):
    new_lst.append(lst[i])
print(new_lst)

#Bai7
t1 = (1, 2, 3)
t2 = (4, 5)
t3 = t1 + t2
print(t3)

#Bai8
d = {}
for i in range(3):
    name = input("Tên: ")
    age = int(input("Tuổi: "))
    d[name] = age
print(d)

#Bai9
lst = [1,2,2,3,1]
result = []
for x in lst:
    if x not in result:
        result.append(x)
print(result)

#Bai10
lst = [1,2,2,3,3,3,4]
max_count = 0
most = None
for x in lst:
    if lst.count(x) > max_count:
        max_count = lst.count(x)
        most = x
print("Phần tử xuất hiện nhiều nhất:", most)

