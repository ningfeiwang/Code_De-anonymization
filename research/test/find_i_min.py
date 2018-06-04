#! /usr/bin/env python
#coding=utf-8

import random

class RandomSelect(object):
    def Partition(self,a, p, r):
        x=a[r]
        i=p-1
        for j in range(p, r):        
            if a[j]<=x:
                i=i+1
                a[i], a[j]=a[j], a[i]
        a[i+1], a[r]=a[r], a[i+1]
        return i+1    

    def RandomPartition(self,a, p, r):
        i=random.randint(p, r)
        a[r], a[i]=a[i], a[r]
        return self.Partition(a, p, r)

    def randomSelect(self,a,p,r,i):
        if p==r:
            return a[p]
        q=self.RandomPartition(a,p,r)
        k=q-p+1
        if i==k:
            return a[q]
        elif i<k:
            return self.randomSelect(a,p,q-1,i)
        else:
            return self.randomSelect(a,q+1,r,i-k)

if __name__ == '__main__':
    a=[random.randint(0,20) for i in range(10)]
    print a

    r=RandomSelect()
    r.randomSelect(a,0,len(a)-1,3)
    print a[2]
    a=sorted(a)
    print a