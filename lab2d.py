#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print(f"Usage:", sys.argv[0], "name age")
    sys.exit()
    
print('Hi', sys.argv[1] + ', you are ' + sys.argv[2], 'years old.')
sys.exit()