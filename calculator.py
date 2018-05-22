#!/usr/bin/env python3

import sys

def rateAndQD(taxableIncome):
    if taxableIncome <= 0: 
        rate, QD = 0, 0
    elif taxableIncome > 0 and taxableIncome <= 1500:
        rate, QD = 0.03, 0
    elif taxableIncome > 1500 and taxableIncome <= 4500:
        rate, QD = 0.1, 105
    elif taxableIncome > 4500 and taxableIncome <= 9000:
        rate, QD = 0.2, 555
    elif taxableIncome > 9000 and taxableIncome <= 35000:
        rate, QD = 0.25, 1005
    elif taxableIncome > 35000 and taxableIncome <= 55000:
        rate, QD = 0.3, 2755
    elif taxableIncome > 55000 and taxableIncome <= 80000:
        rate, QD = 0.35, 5505
    else:
        rate, QD = 0.45, 13505
    return rate, QD
if __name__ == "__main__":
    for arg in sys.argv[1:]:
        try:
            idNum = int(arg.split(":")[0])
            income = int(arg.split(":")[1]) 
    except:
        print("Parameter Error")
    
    taxableIncome = income*0.835 - 3500
    rate, QD = rateAndQD(taxableIncome)
    taxPayable = taxableIncome * rate - QD 
    salaryGet = income*0.835 - taxPayable  
    print("%d:%.2f"%(idNum, salaryGet))
    

