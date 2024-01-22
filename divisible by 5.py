#adding up some title 
print('\nDISPLAY WHICH NUMBER IS DIVISIBLE BY 5.')
print('Given: [10, 20, 33, 46, 55]\n')

#given list of the numbers
given_numbers = list()
#given list of the numbers
given_numbers.append(10)
given_numbers.append(20)
given_numbers.append(33)
given_numbers.append(46)
given_numbers.append(55)

#function to identify which is divisible by 5 
for given in given_numbers:
    if given % 5 ==0:
       print('Number that is divisible by 5: ', given)