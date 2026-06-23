# ISBN-13 codes are used to uniquely identify books. 
# They are made of 12 digits that carry data and 
# a thirteenth check digit which is used to check it is a valid ISBN number.

# The algorithm required to check if an ISBN-13 number is valid is:
# Add the 1st, 3rd, 5th, 7th, 9th and 11th numbers. Call the sum of these odds.
# Multiply the 2nd, 4th, 6th, 8th, 10th and 12th numbers by 3 and then add the products together. 
# Call the answer to this step evens.
# Add odds to evens and then divide by 10. Store the remainder.
# If the remainder is 0 and the 13th digit (the check digit) is 0, 
# then the ISBN-13 number is valid,
# otherwise, to be valid, the check digit should be equal to 10 minus the remainder.

# Task:
# Write a program that creates the ISBN check digits. 
# Your program should output the check digit as an integer 
# when provided with the first 12 digits of what will be an ISBN-13 number.

# Example Input:
# 978150840984

# Example output:
# 9781508409847

# Example Input:
# 978073342609

# Example output:
# 9780733426094



isbn = input('Please input the ISBN number:')
odds = int(isbn[0])+int(isbn[2])+int(isbn[4])+int(isbn[6])+int(isbn[8])+(int(isbn[10]))
evens = int(isbn[1])*3+int(isbn[3])*3+int(isbn[5])*3+int(isbn[7])*3+int(isbn[9])*3+(int(isbn[11]))*3
remainder = (odds+evens)%10
if remainder == 0:
	print(isbn+str(remainder))
else:
	print(isbn+str(10-remainder))