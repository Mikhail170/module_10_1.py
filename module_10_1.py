import threading
import time
from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'a') as file:
        word_number = 1
        for i in range(word_count):
            file.write(f'Слово № {word_number} \n')
            time.sleep(0.1)
            word_number += 1
    print(f'Завершилась запись в файл {file_name}')


time_start = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_finish = time.time()
time_process = time_finish - time_start
print(f'Работа потоков: {time_process}')

time_start2 = time.time()

first_thread = Thread(target=write_words, args=(10, 'example5.txt'))
second_thread = Thread(target=write_words, args=(30, 'example6.txt'))
third_thread = Thread(target=write_words, args=(200, 'example7.txt'))
fourth_thread = Thread(target=write_words, args=(100, 'example8.txt'))

first_thread.start()
second_thread.start()
third_thread.start()
fourth_thread.start()

first_thread.join()
second_thread.join()
third_thread.join()
fourth_thread.join()

time_finish2 = time.time()
time_process2 = time_finish2 - time_start2

print(f'Работа потоков: {time_process2}')



