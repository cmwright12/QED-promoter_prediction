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