count = int(input("Number of items: ")) 
prices = [] 
for i in range(count):  
    price = float(input("Price of item " + str(i + 1) + ": "))    
    if price < 0: 
       print("Invalid price") 
       break 
       prices.append(price) 
else: 
    subtotal = sum(prices)  
    if subtotal >= 5000:  
          rate = 0.10  
    elif subtotal >= 2000: 
          rate = 0.05 
    else:  
          rate = 0  
          discount = subtotal * rate 
          print("Subtotal: Rs.", subtotal)  
          print("Discount: Rs.", discount)  
          print("Final amount: Rs.", subtotal - discount)