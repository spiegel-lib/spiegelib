#!/usr/bin/env python
"""
Utility Functions
"""


import re


"""
Natural Sorting from https://stackoverflow.com/questions/5967500/how-to-correctly-sort-a-string-with-a-number-inside
"""
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]
