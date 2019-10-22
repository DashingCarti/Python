import random  # Imports the library

amount = input("How much would you like to pay? ")  # Asks for the amount to pay

tip = [
    "15",
    "18",
    "20"
]  # Different values of tip

random_tip = random.choice(tip)  # Randomly picks up a tip amount from the given tip values
print(f"Maybe you should pay a tip of {random_tip}%!")  # Prints the tip amount

true_amount = amount.replace("$", "") # Replaces the $ to empty value

final_amount = float((float(random_tip) / 100)) * float(true_amount)  # Calculates the exact tip amount

print(f"The final amount of your tip will be {final_amount}")  # Prints the tip amount
