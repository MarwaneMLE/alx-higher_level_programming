#!/usr/bin/python3
ch = 97
while(ch < 123):
    if chr(ch) != 'e' and chr(ch) != 'q':
        print(chr(ch), end="")
    ch += 1

