units = int(input("Enter units: "))
if units < 0:
        print("Invalid units") 
elif units <= 100:
        bill = units * 2 
elif units <= 200: 
       bill = 200 + (units - 100) * 3 
else:    
    bill = 500 + (units - 200) * 5 
if units >= 0: 
    print("Electricity bill: Rs.", bill)