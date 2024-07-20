from threading import *
from time import sleep
'''Multithreading in Python allows you to execute multiple threads
(smaller units of a process) concurrently.
Python has a Global Interpreter Lock (GIL),
which means that only one thread can execute Python
bytecode at a time in a single process.
However, multithreading can still be useful in certain situations,
such as when you have I/O-bound tasks
where threads can wait for external resources without blocking the entire program.'''
class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)


t1 = hello()
t2 = hi()
t1.start()#t1.run()
sleep(0.2) # sleep method (stop)
t2.start()#t2.run()

t1.join() # we are saying to main thread that wait for some time.
t2.join()

print("Main thread")


