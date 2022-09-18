import time
import os, psutil
process = psutil.Process(os.getpid())
t_start = time.perf_counter()
f=open('input.txt')
n=int(f.readline())
f.close()
def F(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n>1:
        return F(n-1)+F(n-2)
a=F(n)
x=open('output.txt', 'w')
x.write(str(a))
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print(process.memory_info().rss)