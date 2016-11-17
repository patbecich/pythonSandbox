
f = open("/Users/patrick/python/illiad.txt", "r")

print f

ll = f.readlines()

#print range(10)

#for num in range(10):
#    print "num: "+`num`


again = True

while(again):
    counted = raw_input("Character or string to be counted in The Illiad: ")

    periodCount = 0

    for l in ll:
        periodCount = periodCount + l.lower().count(counted.lower())

    print "Number of "+counted+" in the Illiad: "+`periodCount`

    again = raw_input("Again?") == "y"

print "goodbye"

#    x = raw_input("Again?")
#    if x == "y":
#        again = True
#    else:
#        again = False



f.close()

