#第一问：
codon_dict={}
f1=open('codon.txt','r')
lines1=f1.readlines()
for line in lines1:
    if line=='codon   amino\n':
        pass
    elif len(line)==6:
        codon=line[0]+line[1]+line[2]
        codon_dict[codon]=line[4]
    else:
        codon=line[0]+line[1]+line[2]
        codon_dict[codon]='stop'
#第二问：转录
def transcript(DNA):
    for s in DNA:
        #X作为辅助，从而实现正确的替换
        s1=DNA.replace('A','U')
        s2=s1.replace('T','A')
        s3=s2.replace('C','X')
        s4=s3.replace('G','C')
        mRNA=s4.replace('X','G')
    return mRNA
#第三问：翻译
def translate(DNA):
    mRNA=transcript(DNA)
    if 'AUG' not in mRNA:      
        return ''
    else:
        amino=''
        start=mRNA.find('AUG')
        for i in range(start,len(mRNA),3):
            if len(mRNA)-i<3:
                break
            else:
                m=mRNA[i]+mRNA[i+1]+mRNA[i+2]
            if codon_dict[m]=='stop':
                break
            else:
                amino+=codon_dict[m]
        return amino
#第四问
seq_dict={}
ff=open('seq.fa','r')
lines2=ff.readlines()
lines2_new=[]
l1=lines2[0].replace('\n','')
lines2_new.append(l1.replace('>',''))
l2=lines2[1].replace('\n','')
lines2_new.append(l2)
l3=lines2[2].replace('\n','')
lines2_new.append(l3.replace('>',''))
l4=lines2[3].replace('\n','')
lines2_new.append(l4)
seq_dict[lines2_new[0]]=lines2_new[1]
seq_dict[lines2_new[2]]=lines2_new[3]
#第五问
protein_dict={}
protein_dict['seq1']=translate(lines2_new[1])
protein_dict['seq2']=translate(lines2_new[3])
#第六问
fff=open('protein.txt','w+')
fff.write('seq1\n')
fff.write(protein_dict['seq1']+'\n')
fff.write('seq2\n')
fff.write(protein_dict['seq2'])