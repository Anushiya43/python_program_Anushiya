
insulin="FVNQHLCGSHLVEALYLVCGERGFFYTPKTR"

pka={
    "Cterm": 3.65,   
    "Nterm": 8.0,    
    "K": 10.5,       
    "R": 12.4,       
    "H": 6.0,       
    "D": 4.1,       
    "E": 4.1,        
    "C": 8.3,        
    "Y": 10.1        
}

aa_count={
    "K": insulin.count("K"),  
    "R": insulin.count("R"),  
    "H": insulin.count("H"),  
    "D": insulin.count("D"),  
    "E": insulin.count("E"),  
    "C": insulin.count("C"),  
    "Y": insulin.count("Y")   
}

def net_charge(pH):
    
    pos=(10**pka["Nterm"]) / (10**pka["Nterm"] + 10**pH) \
        + aa_count["K"] * (10**pka["K"]) / (10**pka["K"] + 10**pH) \
        + aa_count["R"] * (10**pka["R"]) / (10**pka["R"] + 10**pH) \
        + aa_count["H"] * (10**pka["H"]) / (10**pka["H"] + 10**pH)

    
    neg=(10**pH) / (10**pka["Cterm"] + 10**pH) \
        + aa_count["D"] * (10**pH) / (10**pka["D"] + 10**pH) \
        + aa_count["E"] * (10**pH) / (10**pka["E"] + 10**pH) \
        + aa_count["C"] * (10**pH) / (10**pka["C"] + 10**pH) \
        + aa_count["Y"] * (10**pH) / (10**pka["Y"] + 10**pH)

    return pos-neg 
    
pH = 0
while pH <= 14:
    charge = net_charge(pH)
    print(f"pH = {pH:2d} -> Net Charge = {charge:.2f}")
    pH += 1 

