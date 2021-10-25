#other ways to work in a list

#instead of using a for loop, we can use a list comprehension
languages = ["Python", "Perl", "C++", "Java", "C"]

lengths = [len(language) for language in languages] #this will create a list of the lengths of each language
print(lengths)

#we can also work like this
z = [x for x in range(0,101) if x % 3 == 0] #this will create a list of all the numbers divisible by 3
print(z)

#in this case, we used a list comprehension to create a list of all
#odd numbers between 0 and n
def odd_numbers(n):
	return [x for x in range(0, n + 1) if x % 2 != 0]