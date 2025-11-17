def verify_height(height):
    trade = 0
    repair = 0
    for h in height:
        if h < 50:
            trade += 1
        elif h > 85:
            repair += 1

    return trade, repair

heights = []
num_poles = int(input("Input the number of poles a be avaliable: "))
for i in range(num_poles):
    height = int(input(f"Input the height of pole {i+1}: "))
    heights.append(height)

trade, repair = verify_height(heights)
    

print("\nResults: ")
print("The number of the poles a be replace: ", trade)
print("The number of the poles a be repaired: ", repair)
