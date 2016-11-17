print "Hello, World!"

task = 'y'

while task == 'y':

    name = raw_input("What is your name?")

    name_list = list(name)

    letter = int(input("Which letter?"))-1

    print name_list[letter]
    task = raw_input("again?")
