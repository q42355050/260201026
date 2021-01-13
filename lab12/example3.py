class DNA:    
    def __init__(self, dna_string):
        self.dna_string = dna_string
    
    count_A = 0
    count_C = 0
    count_G = 0
    count_T = 0
    
    def count_nucleotides(self):       
        count_dict = {}
        count_A = 0
        count_C = 0
        count_G = 0
        count_T = 0
        
        for i in self.dna_string:
            
            if i == "A":
                count_A += 1
            if i == "C":
                count_C += 1
            if i == "G":
                count_G += 1
            if i == "T":
                count_T += 1
            
        count_dict["A"] = count_A
        count_dict["C"] = count_C
        count_dict["G"] = count_G
        count_dict["T"] = count_T
        
        return count_dict
        
    def calculate_complement(self):
        
        complement = ""
        
        for i in self.dna_string:
            
            if i == "A":
                complement += "T"
            if i == "C":
                complement += "G"
            if i == "G":
                complement += "C"
            if i == "T":
                complement += "A"
        
        return complement
        
    
    def count_point_mutations(self, dna_):        
        distance = 0
        
        if len(self.dna_string) == len(dna_.dna_string):
            for i in range(len(self.dna_string)):                
                if self.dna_string[i] != dna_.dna_string[i]:
                    distance += 1
            return distance
        
        else: return
        
        
    def find_motif(self, dna_):
        motif_list = []
        length = len(dna_.dna_string)

        for i in range(len(self.dna_string) - length):
            
            if dna_.dna_string == self.dna_string[i:i+length]:
                motif_list.append(i)
        return motif_list
            
                
dna1 = DNA("ACGGGGTGACGCCGCGTGGACTTGAATCG")
dna2 = DNA("AGAGCACTACTGACGCCCCGCGCGATATCGCGCAAAATTTGAAACGCATG")
dna3 = DNA("GAGCC")
dna4 = DNA("CATCG")
dna5 = DNA("TGA")
dna6 = DNA("GATATATGCATATACTT")
dna7 = DNA("ATAT")

print(dna3.count_point_mutations(dna4))
print(dna6.find_motif(dna7))