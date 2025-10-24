
insulin_name="Human Insulin"          
molecular_weight=5808                     
molecular_weight_precise=5808.05          


print("Insulin Name:", insulin_name)
print("Approximate Molecular Weight (int):", molecular_weight)
print("Precise Molecular Weight (float):", molecular_weight_precise)
print("-" * 50)


preproinsulin=(
    "MALWMRLLPLLALLALWGPDPAAA"        # signal peptide (1–24)
    "FVNQHLCGSHLVEALYLVCGERGFFYTPKA"  # B chain (25–54)
    "RREAEDLQVGQVELGGGPGAGSLQPLALEGSLQ"  # C peptide (55–89)
    "KR GIVEQCCTSICSLYQLENYCN"        # A chain (90–110)
)

print("Preproinsulin sequence length:", len(preproinsulin))
print("-"*50)


signal_peptide=preproinsulin[0:24]   
b_chain=preproinsulin[24:54]         
a_chain=preproinsulin[54:86]         


insulin_sequence=b_chain+a_chain


print("Signal Peptide:", signal_peptide)
print("B Chain:", b_chain)
print("A Chain:", a_chain)
print("Mature Insulin Sequence:", insulin_sequence)
print("Length of Mature Insulin:", len(insulin_sequence))
print("-"*50)


molecular_weight=5808      
moles=2


total_weight=molecular_weight*moles
print(f"If you have {moles} moles of insulin, total weight = {total_weight} grams")
print("-"*50)


try:
    
    result=molecular_weight/0
    print("Result:", result)

except ZeroDivisionError as e:
    print("Exception caught! You cannot divide by zero.")
    print("Error message:", e)
