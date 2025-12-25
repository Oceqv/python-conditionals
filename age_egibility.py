# Small exercise with If and Else and also an shorter way of writing this code.
age = 22
if age >= 18:
    message = "Eligible"  # To make this cleaner we use message instead of print
else:
    message = "Not Eligible"
print(message)


# This way it makes it short and clean.
age = 22
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)
