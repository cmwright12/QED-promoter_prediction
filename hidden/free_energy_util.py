
# coding: utf-8

# In[ ]:

dna = 'CGTTGA'
 
pairs = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

def comp(string):
    complement = ""
    for char in string:
        complement += pairs[char]
    return complement
    
def revcomp(string):
    return comp(string)[::-1]
         
dinuc_53 = ['AA', 'AT', 'TA', 'CA', 'GT', 'CT', 'GA', 'CG', 'GC', 'GG']
energy_val = [-1.00, -0.88, -0.58, -1.45, -1.44, -1.28, -1.30, -2.17, -2.24, -1.84]

d53 = {}
for i in range(len(dinuc_53)):
    d53[dinuc_53[i]] = energy_val[i]




#######
def nt_to_fe(dnt):

    pairs = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

    def comp(string):
        complement = ""
        for char in string:
            complement += pairs[char]
        return complement
        
    def revcomp(string):
        return comp(string)[::-1]
             
    dinuc_53 = ['AA', 'AT', 'TA', 'CA', 'GT', 'CT', 'GA', 'CG', 'GC', 'GG']
    energy_val = [-1.00, -0.88, -0.58, -1.45, -1.44, -1.28, -1.30, -2.17, -2.24, -1.84]

    try:
        idx = dinuc_53.index(dnt)
    except:
        idx = dinuc_53.index(revcomp(dnt))    
    return energy_val[idx]
###########    
    
    
def conv_to_energy1(dna):    
    energy_sum = 0
    for i in range(len(dna)-1):
        if dna[i:i+2] in d53.keys():  # is the dinucleotide in the dictionary
            energy_sum += d53[dna[i:i+2]]
        elif revcomp(dna[i:i+2]) in d53.keys():  # is its reverse complement in the dictionary
            energy_sum += d53[revcomp(dna[i:i+2])]
    return format(energy_sum + 0.98 + 1.03, '.2f')
  
def conv_to_energy2(dna):    
    energy_sum = sum( d53[dna[i:i+2]] if dna[i:i+2] in d53.keys() else d53[revcomp(dna[i:i+2])] for i in range(len(dna)-1) )
    return format(energy_sum + 0.98 + 1.03, '.2f')
    
print("dna:", dna)
print(conv_to_energy2(dna))

