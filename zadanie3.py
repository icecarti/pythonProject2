f=open('input.txt')
n=int(f.readline())
f.close()
F=[0]*(n+2)
F[0]=0
F[1]=1
for i in range(2,n+2):
    F[i]=(F[i-1]+F[i-2])%10
a=F[n]
x=open('output.txt', 'w')
x.write(str(a))