preproinsulin = (
    "MALWMRLLPLLALLALWGPDPAAA"   
    "FVNQHLCGSHLVEALYLVCGERGFFYTPKA" 
    "RREAEDLQVGQVELGGGPGAGSLQPLALEGSLQ"  
    "KR GIVEQCCTSICSLYQLENYCN"  
)

print("Full preproinsulin sequence:")
print(preproinsulin)
print("Length of preproinsulin:",len(preproinsulin))
print("-" * 60)


signal_peptide = preproinsulin[0:24]   
b_chain = preproinsulin[24:54]         
c_peptide = preproinsulin[54:89]       
a_chain = preproinsulin[89:110]        

print("Signal peptide:",signal_peptide)
print("B chain:",b_chain)
print("C peptide:",c_peptide)
print("A chain:",a_chain)
print("-" * 60)


insulin = b_chain + a_chain

print("Mature human insulin sequence:")
print(insulin)
print("Length of mature insulin:",len(insulin))

if "A" in insulin and "C" in insulin:
    print("Sequence contains amino acids–extraction successful!")
else:
    print("Error: Something went wrong with sequence slicing.")
