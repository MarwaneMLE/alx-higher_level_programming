#!/usr/bin/python3
"""Saving arguments to a list"""
import sys
import os.path


args = sys.argv[1:]

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

list1 = []

if os.path.exists("./add_item.json"):
    list1 = load_from_json_file("add_item.json")

save_to_json_file(list1 + args, "add_item.json")
