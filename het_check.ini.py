import sys
import numpy as np
import argparse
import math as m

parser = argparse.ArgumentParser()
parser.add_argument("-lrt",help="lrt threshold",default=2)
parser.add_argument("-r",help="collapsed region")
parser.add_argument("-p",help="prob of success",default=0.95)

args = parser.parse_args()

ctH=0
ctD=0
ctT=0
r=0

#ratio=[]
for line in sys.stdin:
    line=line.rstrip()
    vals=line.split()
    #ref=vals[8]
    counts = [(int(vals[3]), 'A'), (int(vals[4]),'C'), (int(vals[5]),'G'), (int(vals[6]),'T')]
    counts.sort()
    if counts[-1][0]==0 or counts[-2][0]==0:
        continue
    r=counts[-1][0]/(counts[-2][0]+counts[-1][0])
    #ratio.append(r)
    if r<=0.71 and r>= 0.61:
        ctD=ctD+1
    elif r<=0.55:
        ctH=ctH+1
    else:
        ctT=ctT+1


#p=float(args.p)
#coef=(m.factorial(ctD+ctT) * m.factorial(ctH)) / (m.factorial(ctH+ctT) * m.factorial(ctD))
#lrt= coef * (p**(ctD-ctH)) * ((1-p)**(ctH-ctD))
#    print("\t".join([line,str(ratio)]))
#r=np.array(ratio)
#print(len(r[np.where(r>0.609)] )) 

lrt=ctD/max(1,ctH)

if lrt>int(args.lrt):
    print(args.r+"\tpass\t"+str(lrt))
else:
    print(args.r+"\tfail\t"+str(lrt))

