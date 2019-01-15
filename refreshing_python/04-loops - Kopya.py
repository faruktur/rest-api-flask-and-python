my_var = "hello world"

for c in my_var:
    print(c)

user_wants_number = True

while user_wants_number == True:
    user_input = input("Should we print again? (y/n)")
    if user_input=="n":
        user_wants_number=False
