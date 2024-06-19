# Starting a Thread

import logging # โมดูลที่ใช้ในการบันทึกข้อความ
import threading # โมดูลที่ใช้ในการสร้างและจัดการเธรด
import time # โมดูลที่ใช้ในการจัดการกับเวลา

def thread_function(name):
    logging.info("Thread %s: starting", name) # บันทึกข้อความเมื่อเริ่มทำงาน
    time.sleep(2) # หยุด 2 sec
    logging.info("Thread %s: finishing", name) # บันทึกอีกคครั้งเมื่อทำงานเสร็จ

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s" # กำหนดรูปแบบของข้อความที่บันทึก โดยจะแสดงเวลาปัจจุบันและข้อความ
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S") 

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,)) #สร้างเธรดใหม่โดยให้ target เป็นฟังก์ชัน thread_function และส่งอาร์กิวเมนต์ (1,) ให้กับฟังก์ชันนั้น
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")
