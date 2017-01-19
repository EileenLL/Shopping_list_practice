x = "Eileen"
y = "Leeza"

if len(x) > len(y):
    print "My name is greater!"
elif len(y) > len(x):
            print "Their name is greater"
else:
    print "Our names are equal"

# New Program about date
date = 18
if date >= 30/2:
    print "Oh, we're halfway there!"
else:
    print "The month is still young"

#3

today = "Wednesday"
if today == "Monday":
    print "Yaaas Monday! Here we go!"
elif today == "Tuesday":
    print "Sigh, it's only Tuesday."
elif today == "Wednesday":
    print "Humpday!"
elif today == "Thursday":
    print "#tbt"
elif today == "Friday":
    print "TGIF!"
else:
    print "Yeah, it's the weekend!"

#4

age = 28
if age >= 18 and age >= 21:
    print "Yay! I can vote and go to a bar"
elif age >= 18 and age < 21:
    print "I can vote but cannot go to a bar."
else:
    print "I cannot vote or go to a bar."

#5

x = 8
if x % 2 == int():
    print "The number 8 is even."
else:
    print "The number 8 is odd."
# 5.2

x = 8
if x % 3 == int():
    print "The number 8 is odd."
else:
    print "The number 8 is even."

# 5.3

x = 8
y = 9
if x % 2 == int() and y % 2 == int():
    print "Both numbers are even."
else:
    print "Both numbers are not even."

#5.4

x = 8
y = 9
if x % 2 == int() and y % 2 == int():
    print "Both numbers are even."
elif x % 2 == int() and y % 3 == int():
    print "8 is even and 9 is odd."
elif y % 2 == int() and x % 3 == int():
    print "8 is odd and 9 is even."
else:
    print "Both numbers are odd."

#6

favorite_color = raw_input("What is your favorite color? ")

if str.lower(favorite_color) == "blue":
    print "My favorite color is blue!"
else:
    print "My favorite color is not blue."

#7

fav_color = raw_input("What's your favorite color? ").capitalize()

if (fav_color == "Blue" or fav_color == "Red" or fav_color == "Yellow"):
    print "My favorite color is primary"
else:
    print "My favorite color is secondary"
