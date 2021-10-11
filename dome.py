import time,threading
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i) +" ")
        my_sum += i
        #time.sleep(0.1)
    return my_sum
# 创建一个包含4条线程的线程池
with ThreadPoolExecutor(max_workers=80) as pool:
    # 使用线程执行map计算
    # 后面元组有3个元素，因此程序启动3条线程来执行action函数
    results = pool.map(action, range(10000))
    print('--------------')
    for r in results:
        print(r)