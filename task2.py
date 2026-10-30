name = input("Employee name: ") 
basic = float(input("Basic salary: ")) 
if basic < 0: 
       print("Invalid salary") 
else:    
      hra = basic * 0.20 
da = basic * 0.10  
gross = basic + hra + da   
deduction = gross * 0.05   
net = gross - deduction   
print("Employee:", name)   
print("Gross salary: Rs.", round(gross, 2))   
print("Deduction: Rs.", round(deduction, 2))   
print("Net salary: Rs.", round(net, 2))