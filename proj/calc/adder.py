"""Ask for integer input and print the sum. Empty string terminates input."""
sum = 0
any = False

while True:
    raw = input("Number: ")
    if not raw: 
        break
    try:
        sum += int(raw)
    except ValueError:
        print(f"Sorry, {raw} isn't an integer")
    else:
        any = True

if any:
    print(f"Sum is {sum}.")
else:
    print("Sorry, nothing to work with.")

