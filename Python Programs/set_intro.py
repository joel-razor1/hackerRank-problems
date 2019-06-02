from __future__ import division

def average(array):
    # your code goes here
    set1=set(array)
    av=0
    av= sum(set1)/len(set1)
    return av

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result