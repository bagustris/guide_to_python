#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 13:59:50 2018

@author: lindemann
"""

try:
    with open("myfile.txt", "r") as text_file:
        lines = text_file.readlines()
except FileNotFoundError as e:
    print("File", e.filename, "is not found.")
except PermissionError as e:
    print("Permission error: '"+e.strerror+"'")