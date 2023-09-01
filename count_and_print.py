# Python program to count from 1 to 100
for i in range(1, 101):
    # Check if the number is evenly divisible by 5 using the modulo operator (%)
    if i % 5 == 0:
        print("Hit!")
    else:
        print(i)
