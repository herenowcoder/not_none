# Copyright (c) 2011 Wojciech Kaczmarek <wojtekk@kofeina.net>
#
# This code is released under the terms of the BSD 2-Clause License;
# see LICENSE file for details.


class nnattr:
    def __init__(self, subject):
        self.__inner = subject
    def __getattr__(self, attr):
        return None if self.__inner is None else getattr(self.__inner, attr)

class nncall:
    def __init__(self, subject):
        self.__inner = subject
    def __getattr__(self, attr):
        return (lambda:None) if self.__inner is None\
               else getattr(self.__inner, attr)

# Why such split?
#
# Well if attr is a method then not_none should return a wrapped
# function which returns null or calls the original. But how we know
# if the attr has to be a method or just a plain attr? We don't have
# any magic way to know it up front..
#
# so the usage becomes like this:
# 
# nnattr(obj).attr
# nncall(obj).method()


# Other bugs:
# it doesn't delegate __class__ to subject.
