print "Hello?"
x = raw_input("What is your name?")
print "Hello "+x
day = raw_input("How was your day?")
if day == "good" or day == "great":
    print('I am glad!')
else:
    print('I am sad')

y = open("/Users/patrick/python/illiad.txt", "r")
ll = y.readlines()

funct= raw_input("What would you like to do?")

while funct == "math":
    a = input("give number 1")
    b = input("give number 2")
    f= raw_input ("What math function would you like to perform")

    if f == "add":
        print a+b
    if f == "subtract":
        print a-b
    if f == "multiply":
        print a*b
    if f == "divide":
        print a/b
    else:
        print "Error"
#    funct = "count" == raw_input("Again?") == "y"

while funct == "count":
    counted = raw_input("Character or string to be counted in The Illiad: ")

    periodCount = 0

    for l in ll:
        periodCount = periodCount + l.lower().count(counted.lower())

    print "Number of "+counted+" in the Illiad: "+`periodCount`
    funct = raw_input("Now What?")
    break
print "end"    
    
#funct = raw_input("What would you like to do now?")


#task = raw_input("What would you like to do now?")

