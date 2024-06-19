# extending the Thread class and return values
from time import sleep, ctime
from threading import Thread

# custom thread class
class CustomThread(Thread):
    # override the run function
    def run(self):
        #Block for a moment
        sleep(1) # หยุด 1 sec
        #display a message
        print(f'{ctime()} This is coming from another thread') # แสดงเวลาปัจจุบันเมื่อเธรดใหม่แสดงข้อความ
        #Store return value   เก็บค่าที่ต้องการส่งกลับ
        self.value = 99

    #create the thread
thread = CustomThread()
    #start the thread
thread.start()
    #wait for the thread to finish
print(f'{ctime()} Waiting for the thread to finish') # แสดงเวลาปัจจุบันเมื่อเริ่มรอให้เธรดทำงานเสร็จ
thread.join()

    #get thevalue returned from run
value = thread.value
print(f'{ctime()} Got: {value}') # แสดงเวลาปัจจุบันเมื่อเธรดหลักได้รับค่าจากเธรดใหม่ 