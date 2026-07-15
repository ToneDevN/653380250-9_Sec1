age = int(input("Please enter your age: "))
like_action_movie = str(input("Do you like action movies? (yes/no)"))


if (age < 5):
    print("You're too young for movies! Enjoy cartoons.")
elif (age >=5 and age < 12):
    print("G-rated or PG-rated movies.")
elif (age >=5 and age < 12):
    print("PG-13 or R-rated (with parental guidance).")
elif (age >= 18):
    print("Any movie rating.")
else :
    print("")