edad=[ 22 , 19 , 24 , 25 , 26 , 24 , 25 , 24 ]
phrase="I am a teacher and I love to inspire and teach people. love"
print("Point 01\n",set(edad))
words=phrase.split(' ')
single_words=set(words)
print("Point 02")
print("First let's start talking about sequences of lists and sets, all 2 sequences are mutable, that means that they can be modified.The sets is a sequence where\nthe values that are not repeated are stored and to create a set must be enclosed with braces and the lists is a container where it stores the values that \ncan be strings, integers, float, tuples, etc. and to create them must be enclosed with brackets. A tuple is a set where elements are stored in an ordered \nform that cannot be modified, that is to say that they are immutable. To modify a tuple it is necessary to convert it to a list and already converted into a \nlist it can be modified, in a tuple you can store strings, integers, float, etc and they have to be enclosed with parenthesis and the string is a group of \nsequences that are represented by strings of text which to create them you have to use double quotes or single quotes.")
print("Point 03\n",single_words)
