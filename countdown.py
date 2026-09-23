# Ask user for starting number and convert to integer
start_num = int(input("Enter a number to start countdown from: "))

# While loop counting down to 1
count = start_num
while count >= 1:
    print(count)
    count -= 1  # Decrement loop variable to avoid infinite loop

print("Blast off!")
