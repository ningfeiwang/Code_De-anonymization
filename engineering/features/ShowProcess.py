#!/usr/local/lib
# -*- coding: UTF-8 -*-

import sys, time

class ShowProcess():
 
    i = 0 
    max_steps = 0 
    max_arrow = 50 

    # init
    def __init__(self, max_steps):
        self.max_steps = max_steps
        self.i = 0

    # display function
    # [>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100.00%
    def show_process(self, i=None):
        if i is not None:
            self.i = i
        else:
            self.i += 1
        num_arrow = int(self.i * self.max_arrow / self.max_steps) 
        num_line = self.max_arrow - num_arrow 
        percent = self.i * 100.0 / self.max_steps 
        process_bar = '[' + '>' * num_arrow + '-' * num_line + ']'\
                      + '%.2f' % percent + '%' + '\r' 
        sys.stdout.write(process_bar) 
        sys.stdout.flush()

    def close(self, words='finished'):
        print ''
        print words
        self.i = 0

if __name__=='__main__':
    max_steps = 100

    process_bar = ShowProcess(max_steps)

    for i in range(max_steps + 1):
        process_bar.show_process()
        time.sleep(0.05)
    process_bar.close()
