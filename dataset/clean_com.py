#!/usr/local/bin/python
# coding:utf-8

import os
import re

def get_name(filename):
    name_list = os.listdir(filename)
    return name_list


def del_com(name_list):
    for each in name_list:
        if each == ".DS_Store":
            continue
        f = open(os.path.join(path,each),'r')
        lines_f = f.readlines()
        f.close()
        newstr = ''
        for line in lines_f:
            index = line.find("#")
            if index == -1:
                # if line.strip() !='':
                newstr = newstr + line
            else:
                if index != 0:
                    newstr = newstr + line[:index] + '\n'
        if "testing" in path:
            write_con("test_uc_feature", each, newstr)
        else:
            write_con("train_uc_feature", each, newstr)

def write_con(flag, file, content):
    name = file
    if flag == "train_uc_feature":
        f = open(os.path.join("train_uc_feature",name), 'a')
        f.write(str(content))
        f.close()
    else:
        f = open(os.path.join("test_uc_feature",name), 'a')
        f.write(str(content))
        f.close()



if __name__ == '__main__':
    global path
    os.system("mkdir train_uc_feature")
    os.system("mkdir test_uc_feature")
    
    for i in range(0,2):
        if i == 0:
            path = "./testing"
        else:
            path = "./training"
        name_list = get_name(path)
        del_com(name_list)