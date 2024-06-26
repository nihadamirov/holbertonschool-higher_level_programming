#!/usr/bin/python3

"""Replace an element at specific index without modifying the whole list"""


def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list

    copy = [x for x in my_list]
    copy[idx] = element
    return copy
