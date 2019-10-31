import algo
from sys import argv
import numpy as np
from copy import deepcopy as dp
from random import randrange
from os import mkdir, chdir
from os.path import exists
import methods
def find(seat, number):
    for i_index, i in enumerate(seat):
        for j_index, j in enumerate(i):
            if j==number:
                return (i_index, j_index)
    return (-1,-1)
funcdict={'b':algo.shiftDown, 'f':algo.shiftUp, 'l':algo.shiftLeft, 'r':algo.shiftRight, 'fl':algo.shiftLeftUp, 'fr':algo.shiftRightUp, 'bl':algo.shiftLeftDown, 'br':algo.shiftRightDown}
def execute(l, moves, method):
    for move in moves:
        i_index, j_index=find(l, move[0])
        direction=funcdict[move[1]]
        num=move[2]
        l=direction(i_index+1, j_index+1, num, l, method)
    return l
def read_reqs(filename):
    r=[]
    f=open(filename, 'r')
    for line in f.readlines():
        com=line.strip().split()
        r.append((int(com[0]), com[1], int(com[2])))
    f.close()
    return r
if __name__=='__main__':
    try:
        number, times=int(argv[1]), int(argv[2])
    except:
        print("Please input with the correct format:\npython "+__file__+" [number to find] [times to analyse] [filename of requirements(optional)]")
        exit(1)
    try:
        filename=argv[3]
    except:
        filename="requirements.txt"
    reqs=read_reqs(filename)
    poss_rand=np.zeros((6,7))
    poss_swap=np.zeros((6,7))
    poss_push=np.zeros((6,7))
    poss_inst=np.zeros((6,7))
    poss=[poss_rand, poss_swap, poss_push, poss_inst]
    for _ in range(times):
        luckier=randrange(len(reqs))
        reqs=reqs[luckier:]+reqs[:luckier]
        swap=algo.generateSeats() #swap serves as random seat at first, and then does its work
        push=dp(swap)
        inst=dp(swap)
        i_index, j_index=find(swap, number)
        poss_rand[i_index][j_index]+=1
        swap=execute(swap, reqs, methods.swap())
        i_index, j_index=find(swap, number)
        poss_swap[i_index][j_index]+=1
        push=execute(push, reqs, methods.push())
        i_index, j_index=find(push, number)
        poss_push[i_index][j_index]+=1
        inst=execute(inst, reqs, methods.inst())
        i_index, j_index=find(inst, number)
        poss_inst[i_index][j_index]+=1
    print('data generated this time:')
    filname='data'
    if not exists(filname):
        mkdir(filname)
    chdir(filname)
    for index, mode in enumerate(['rand', 'swap', 'push', 'inst']):
        try:
            old=np.array(list(map(int,open(str(number)+"_"+mode+'.txt').read().split())))
        except:
            old=np.zeros(42, dtype=int)
        poss[index]=poss[index].ravel().astype(int)
        print(mode+':', end='')
        for i in poss[index]:
            print(i, end=' ')
            top=poss[index]+old
        with open(str(number)+'_'+mode+'.txt', 'w') as f:
            for i in top:
                f.write(str(i))
                f.write(' ')
        print()
        
