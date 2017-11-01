
#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lamplight'
import threading
from time import sleep

suma = 100

def cat(fun1):
    suma = fun1 - 5
    print("猫吃完后剩下：%s" %suma)
    return suma
    sleep(2)
def dog(fun2):
    suma = fun2 -10
    print("狗吃完后剩余: %s" %suma)
    return suma

threads = []
t1 = threading.Thread(target=cat, args=(suma,))
threads.append(t1)
t2 = threading.Thread(target=dog, args=(suma,))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        #suma = 100
        t.setDaemon(False)
        t.start()

    #print("总共剩下：%s" %suma)
    #
    #

