import pathlib
s=pathlib.Path("D://vishal.txt")
if(s.exists()):
    print("file is already exists")
else:
    f=open("d://vishal.txt","w")
    f.write("this is my new file")
    f.close()
