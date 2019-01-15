

known_people = ["john","anna","mary"]
person = input("enter the person you know:")

if person in known_people:
    print("You know {}!".format(person))
    

if person not in known_people:
    print("You do not know {}!".format(person))
