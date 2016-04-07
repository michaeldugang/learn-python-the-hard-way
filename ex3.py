# this is ex from ex5 to ex8
name = 'Mic Py. Du'
age = 35 #not a lie
height = 60 #inches

print "Let us talk about %s"%name
print "He is %d years old" % age
print "And %d inches" % height

# %r means print anything
print "dsd %r" % (name )

print "Let us talk about %s"%name
print "He is %d years old" % age
print "And %.2f cm" % (height*2.54)

# ex6
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

#ex7
print "Mary had a little lamb."
print "Its fleece wa white as %s." % 'snow'
print "And everywhere that Mary went."
print "."*10 #repeat 10 times of .

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end, try removing it to see what happens
print end1+end2+end3+end4+end5+end6
print end7+end8+end9+end10+end11+end12

#ex8
formatter = "%r %r %r %r"
print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight.")
