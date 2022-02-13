#hola 3 -> holaholahola
#Lunacy 2 -> LunacyLunacy
#ENCB 4 -> ENCBENCBENCBENCB


def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "solo puedes utilizar strings"
        return string * n
    return repeater


def run():
    repeater_5 = make_repeater_of(5)
    print(repeater_5("Hola"))
    repeater_10 = make_repeater_of(10)
    print(repeater_10("Ricardo"))
if __name__ == "__main__":
    run()


#make the follow problem

#def make_division_by(n):
    #"""This closure returns a function that returns the division of an x number by n"""
    #you have to code here
    #pass

#division_by_3= make_division_by(3)
#print(division_by_3(18)) # the expected output is 6 

#division_by_3= make_division_by(5)
#print(division_by_3(100)) # the expected output is 6 

#division_by_3= make_division_by(18)
#print(division_by_3(54)) # the expected output is 6 