# extending the Thread class
from time import sleep, ctime
from threading import Thread

# custom thread class
class CustomThread(Thread):   # สร้างคลาสเธรด
    # override the run function
    def run(self):
        # block for a moment
        sleep(1)  # หยุดการทำงานของเธรดนี้ชั่วคราวเป็นเวลา 1 วินาที
        # display a message
        print(f'{ctime()} This is coming from another thread')

# create the thread
thread = CustomThread()
# start the thread
thread.start()
# wait for the thread to finish
print(f'{ctime()} Waiting for the thread to finish')
thread.join() 