#!/usr/bin/python
# -*- coding: UTF-8 -*-

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]#不明白字符串返回的参数是什么


def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif len(word) > 1 and first(word) != last(word):
        return False
    return is_palindrome(middle(word))

print is_palindrome('tomato')
print is_palindrome('otto')
print is_palindrome('noon')
print is_palindrome('a')

