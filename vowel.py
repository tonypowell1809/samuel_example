import re #   import regular expressions do do checking


#####   Get user input clean up input and do some comparsions

data = input("Enter a letter of the alphabet: ")
data = data.strip() #Remove leading and trailing white space
first_data=data[0]  #After whitespace is removed I only want one character of what is inputed
#in=input()
first_data=first_data.lower()  #function to convert the data to lower

#error checking to make sure that the first character is a letter

if  (first_data.isalpha()):
    print("Alpha")
    print (first_data)


    ['string one', 'string two']
    if first_data in ['a','e', 'i', 'u']: #basically is first_data in the array
       print("vowel") 

    elif first_data in ['y']:
       print("vowel half the time")
    else:
       print ("not a vowel")
