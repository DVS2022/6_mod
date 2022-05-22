import requests
import time
from threading import Thread

def get_html(link):
	text = requests.get(link).text
	print(f'{link} длина текста {len(text)}')

links=['https://google.com/', 'https://yandex.ru/',
		'https://github.com/DVS2022', 'https://brunoyam.com/', 
		'https://mail.ru/']
threads = [Thread(target = get_html, args = (links[i], )) for i in range(5)]
time1 = time.time() 
for t in threads:
	t.start()
	t.join()
print(f'Время последовательно: {time.time()-time1}\n')

threads = [Thread(target = get_html, args = (links[i], )) for i in range(5)]
time1 = time.time()
for t in threads:
	t.start()
for t in threads:
	t.join()
print(f'Время параллельно: {time.time()-time1}')