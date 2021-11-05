#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 常量类
Desc : 
"""


class const():
    def __setattr__(self, name, value):
        if self.__dict__.__contains__(name):
            raise self.ConstError("can't change const.%s" % name)
        if not name.isupper():
            raise self.ConstCaseError("const name '%s' is not all uppercase" % name)

        self.__dict__[name] = value


import sys

sys.modules[__name__] = const()
