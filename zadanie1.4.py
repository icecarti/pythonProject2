f=open('input.txt')
a,b =list(map(int, f.readline().split()))
f.close()
x=open('output.txt', 'w')
x.write(str(a+b**2))
