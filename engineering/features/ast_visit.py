#!/usr/local/bin/python
# coding:utf-8

import ast

class visit(ast.NodeVisitor):

    def writefeatures(self,features):  
        f = open("ast.txt", 'a')
        f.write(str(features))
        f.write(",")
        f.close()

    def generic_visit(self, node):
        
        # print type(node).__name__
        ast.NodeVisitor.generic_visit(self, node)
        self.writefeatures(type(node).__name__)


if __name__ == '__main__':
    expr = """
def add(arg1, arg2):
    return arg1 + arg2
    """
    # test = []
    tree = ast.parse(expr)
    x = visit()
    x.visit(tree)
    # print test