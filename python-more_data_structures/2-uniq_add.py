#!/usr/bin/python3


def uniq_add(my_list=[]):

return sum({elem for elem in my_list if isinstance(elem, int)})
