import time
import os
t="D://hello.html"
ctim=os.path.getctime(t)
ti=os.path.getmtime(t)

ctima=time.ctime(ctim)
cmti=time.ctime(ctima)

print(ctima)
print(cmti)

