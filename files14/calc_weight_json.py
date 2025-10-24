import jsonFileHandler

data = jsonFileHandler.readJsonFile('files14/insulin.json')

if data != "" :
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
    
    aaweights = data['weights']
    
    
    aaCountInsulin = {x: float(insulin.upper().count(x)) for x in [
        'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
        'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'
    ]}
    
    molecularWeightInsulin = sum(aaCountInsulin[x] * aaweights[x] for x in aaCountInsulin)
    print("The rough molecular weight of insulin is:", molecularWeightInsulin)
    molecularWeightInsulinActual = 5808  # example actual weight
    percent_error = ((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100
    print("Percent error:", percent_error)

else:
    print("Error. Exiting program")