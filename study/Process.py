import os
print('Process %s.'%os.getpid())

pid=os.fork()

if pid==0:
    print('Child process:%s,my parent process:%s'%(os.getpid(),os.getppid()))
else:
    print('Child process:%s,my parent process:%s'%(os.getpid(),pid))