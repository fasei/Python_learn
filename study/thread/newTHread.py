import time,threading

#锁
lock=threading.Lock()

#共享数据
local_school = threading.local()


def loop():
    print('loop start.thread name:%s'%threading.current_thread().name)
    n=10
    while n<200:
        lock.acquire()
        n=n+1
        print('I will sleep',n)
        time.sleep(0.1)
        lock.release()
    print('end while')


t=threading.Thread(target=loop,name='haha')
t.start()
t.join()
