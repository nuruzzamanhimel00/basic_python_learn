print('----------- File ------------------')
# f = open("demofile.txt", "rt")
# # print(f.read())
# print(f.readline())
# f.close()

# with open("demofile.txt") as f:
# #   print(f.read())
#     print(f.readline())
#     print(f.readline())

# with open("demofile.txt") as f:
#   for k, v in enumerate(f):
#     print(k, v)

with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

# #open and read the file after the appending:
# with open("demofile.txt") as f:
#   print(f.read())

# f = open("myfile.txt", "x")

with open("demofile.txt", "r") as f:
#   f.seek(5);
#   print(f.read(5))
    print(f.fileno())










