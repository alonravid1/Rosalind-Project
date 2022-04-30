"""
@Author:Aputer

Rosalind Project problem ID: MPRT
"""
import urllib

def get_url(protein):
    link="https://www.uniprot.org/uniprot/"+protein+".fasta"
    f=urllib.request.urlopen(link)
    mf=f.read()
    nf=mf.decode("utf-8")
    nf=nf[nf.find('\n'): ]
    nf=nf.replace('\n','')
    nf='>'+nf
    return(nf)
    
file=open("rosalind_mprt.txt",'r')
f=file.readlines()
g=" ".join(str(x) for x in f)
g=g.replace(" ","")
g=g.split('\n')


def find_motif(protein):
    aminos=get_url(protein)
    positions=[]
    for aa in range(len(aminos)-4):
        if(aminos[aa]=='N' and aminos[aa+1]!='P'):
            if(aminos[aa+2]=='S' or aminos[aa+2]=='T'):
                if(aminos[aa+3]!='P'):
                    positions.append(aa)
    positions=" ".join(str(i) for i in positions)
    return(positions)
for line in g:
    print(line)
    print(find_motif(line))