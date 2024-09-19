subtotal,g_rate = map(float,input("Enter the sobtotal and a gratuity rate: ").split(","))
gratuity = subtotal*(g_rate/100)
total = gratuity+subtotal
print(f"The gratuity is {gratuity:.2f} and the total is {total:.2f}")