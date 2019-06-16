# this program says Hello and ask for name

print('Hello World')
print('what is your name?') # ask for their name
myName = input()
print('it is good to meet you' + myName)
print('the length of your name is:')
print(len(myName))

print('what is your age?') #ask for their age
myAge = input()
print('you will be ' + str(int(myAge)+1) + 'in a year.')