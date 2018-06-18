#!/usr/bin/env python
import re
from scipy import stats
import sys
import multiprocessing as mp
import time
###gobal variables
seq_id = []
e_val = []
protein_search=[]
seq=[]
inp=sys.argv[1]
query=[]
seq_val={}
opt=sys.argv[2]
output=open(opt,'w+')
new_list=[]
### 
with open(inp, 'r') as data:
    for inc in data:
        line= inc.rstrip('\n')
        line= line.lstrip()
        if line.startswith('Query='):
            query.append(line)
        GU0 =    re.search('GU071[0-9]*.1_prot_ADO9[0-9][0-9]*.1.1',line)
        KJ_or_Y= re.search('K[A-Z]0190[0-9]*.1_prot_A[A-Z][A-X][0-9*.1_[1-4]*',line)
        NC_0=    re.search("NC_0[0-4][0-9]*.1_prot_YP_[0-9]*.1_[0-9]*",line)
        J_N_or_F=re.search('J[B-P][0-9]7[0-9][0-9]*.1_prot_AF[A-F[0-9]*.1_[0-4]*',line)
        D_or_HQ= re.search("[D-H]Q[1-9]*.[0-4]_prot_A[A-P][C-Z][0-9*.[0-9]*",line)
        MH=      re.search("MH107246*",line)
        if GU0:
            seq_id.append(GU0.group())  
        elif (KJ_or_Y):
            seq_id.append(KJ_or_Y.group())
        elif (NC_0):
            seq_id.append(NC_0.group())
        elif (J_N_or_F):
            seq_id.append(J_N_or_F.group())
        elif (MH):
            seq_id.append(MH)
        elif (D_or_HQ):
            seq_id.append(D_or_HQ.group())
        newline= re.match('0.0[0-4][0-9]*',line)
        neoin =  re.search('[0-9]e-[0-9][0-9]*',line)
        if neoin:
            neoin=float(neoin.group())
            e_val.append(neoin)
        elif newline:
            newline=float(newline.group())
            e_val.append(newline)
        else: 
            seq.append(line)
        output.write(" %s :  seq_id %s, e value : %s \n " % ( query ,seq_id, e_val))

output.close()
#for key, value in seq_val.items():
#    output.write("%s \n #s " %( key,value))
#output.close()
#for queries in query:
#    for sequence_id in seq_id:
#        for e_values in range(0,len(e_val)):
#            if sequence_id not in new_list:
#                new_list.append((sequence_id,e_val[e_values]))
#                seq_val[queries] = frozenset(new_list)
            #print("seq_val = %s : seq_val[queries] = %s " % (seq_val,str(seq_val[queries])))

#            else:)

                #print(i + '\n' + str(inc) +  str(seq_id[inc]) + ' : ' + str(e_val[incr]) + '\n'  )


#f =open[(opt,"w+")
#for key,increment in seq_val.items():
#    print('query :  %s' % key)
#    print('hugemouns list : %s ' % str(increment))
#    f.write("queries  %s : %s \n" % (key, str(increment))
#f.close()
#if __name__ == '__main__':
#    continue
