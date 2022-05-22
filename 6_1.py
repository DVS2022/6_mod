from threading import *
import time
from datetime import datetime


def get_tread(thread_name):
	time.sleep(1)
	print(thread_name)

t1 = datetime.now()
treads = [Thread(target=get_tread, args=str(i)) for i in range(5)]

for t in treads:
	t.start()
	t.join()

print('Время выполнения команды:', (datetime.now() - t1))
