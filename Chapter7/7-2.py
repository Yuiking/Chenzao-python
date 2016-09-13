#!/usr/bin/python
# -*- coding: UTF-8 -*-

def eval_loop():
    while True:
        x = raw_input('>')
        if x == 'done':
            break
        print eval(x)

eval_loop()