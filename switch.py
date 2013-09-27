#!/usr/bin/python

file = open('source', 'r')
source = file.readlines()
source = [int(i.strip(), 2) for i in ram]

ram = 300 * [0]
ip = 0

ops = [ 'Load', 'Store', 
        'Input', 'Output', 
        'Input Addr', 'Outp. Addr', 
        'Add', 'Subtract', 'Multiply', 'Divide', 
        'Shft Left', 'Shft Right', 
        'Increment', 'Decrement', 
        'Jump', 'Jump if 0', 'Jmp if neg', 
        'Halt']

for i in source:
    ip += 1
    var = i & (16 - 1)
    op = ops[(i & ((16 - 1) << 4)) >> 4]

    print 'Operator is: ' + op + '\t\t' + \
          'Variable is: ' + str(var)
