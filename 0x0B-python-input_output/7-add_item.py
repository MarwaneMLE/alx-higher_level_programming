#!/usr/bin/python3
"""Saving arguments to a list"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    list1 = load_from_json_file("add_item.json")
except FileNotFoundError:
    list1 = []

for i in sys.argv[1:]:
    list1.append(i)
save_to_json_file(list1, "add_item.json")
