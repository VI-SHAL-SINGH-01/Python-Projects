import time
for i in range(1,20):
    if(i==5):
        print("this is my break point",i)
        time.sleep(2)
        print(a)
        continue
    if(i==10):
        print("this is my break point",i)
        #time.sleep(2)
        continue
        time.sleep(2)
    if(i==15):
        print("this is my break point",i)
        time.sleep(2)
        continue
    if(i==17):
        print("this is my break point",i)
        break
    print(i)
