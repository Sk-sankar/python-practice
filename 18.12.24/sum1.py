# # file=open("textfile","w")

# # print(file.write("\n iam sankar"))

# # file.close()

# # f=open("textfile","a")

# # print(f.write(" \n khk"))
# # print(f.read())


# f=open("textfile","r+")

# print(f.readline())

# for i in range(1, 6, 2):
#     print(i, end=' ')

# count = 0
# while count < 3:
#     count += 1
#     if count == 2:
#         continue
#     print(count, end=' ')

# for i in range(5):
#     if (i % 2 == 0):
#         continue
#     print(i, end=' ')

for i in range(5):
    if (i % 2 == 0):
        continue
    print(i, end=' ')