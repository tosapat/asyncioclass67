# running a function with arguments in another thread
from time import sleep, ctime
from threading import Thread

# a custom function that blocks for a moment
def task(sleep_time, message):  # ฟังก์ชันที่เราจะให้เธรดใหม่เรียกใช้ โดยมีพารามิเตอร์สองตัวคือ sleep_time และ message
    # block for a moment
    sleep(sleep_time)
    # display a message
    print(f'{ctime()} {message}')

# create a thread
thread = Thread(target=task, args=(1.5, 'New message from another thread'))  #หยุดการทำงานเป็นเวลา 1.5 วินาที แล้วแสดงข้อความ New message ดังนั้นใน fucytion มี sleep time จึงหยุดการทำงาน 1.5  sec
# run the thread
thread.start()
# wait for the thread to finish
print(f'{ctime()} Waiting for the thread...') # จะแสดงตัวแรก
thread.join()