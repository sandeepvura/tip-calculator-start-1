#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("welcome to tip calculator")
bill = input("total bill: ")
split =input("how many people should split the total bill: ")
tip = input("how much tip are you paying: ")

bill_as_float = float(bill)
split_as_int = int(split)
tip_as_float = float(tip)
result = print((bill_as_float / split_as_int) * tip_as_float)

