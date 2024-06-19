# running a function in another thread
from time import sleep,ctime
from threading import Thread

# a custom fuction that blocks for a moment
def task(): # สร้างเพื่อใช้งาน thread ใหม่
    # block for a moment
    sleep(1) # หยุดการทำงาน 1 sec
    # display a message  
    print (f'{ctime()} This is from another thread') # แสดงข้อความพร้อมเวลาปัจจุบัน

# create a thread
thread = Thread (target=task) # การสร้าง thread 
# run the thread
thread.start()
# wait for the thread to finish
print (f'{ctime()} Waiting for the thread...') # ตัวนี้จะแสดงก่อนเพราะไม่ต้องรอแต่ทั้งสองตัวทำงานพร้อมกัน
thread.join() 









