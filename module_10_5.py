import multiprocessing
from datetime import datetime
# 0:00:04.608078
# 0:00:02.566816


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while file.readline():
            all_data.append(file.readline())
    print(all_data)
files_name = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

if __name__ == '__main__':
    # start_time = datetime.now()
    # for i in files_name:
    #     read_info(i)
    # end_time = datetime.now()
    # print(end_time - start_time)

    start_time = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files_name)
    end_time = datetime.now()
    print(end_time - start_time)