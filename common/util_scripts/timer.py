import time
from functools import wraps

#装饰器函数，用于统计程序运行时间
def timer(func):
    @wraps(func)
    def wraper(*args,**kwargs):
        start_time=time.time()
        print(time.localtime(start_time))
        print(f'程序开始运行时间:{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(start_time))}')
        result=func(*args,**kwargs)
        end_time=time.time()
        final_time=end_time-start_time
        print(f'程序结束运行时间:{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(end_time))}')
        sec=final_time/60
        print(f'程序总运行时间为:{final_time:.2f}秒,约为{sec:.2f}分钟')
        return result
    return wraper
if __name__=='__main__':

    @timer
    def addd():
        time.sleep(1)
        result=1+1
        return result
    a=addd()