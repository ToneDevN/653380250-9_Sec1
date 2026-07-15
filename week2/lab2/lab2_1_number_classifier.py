def number_classifier(number: int) -> str:
    if (number > 0) :
        return "positive"
    elif (number < 0) :
        return "negative"
    else: return "zero"

def check_odd_even(number: int) -> str:
    if (number % 2 == 0) :
        return "even"
    else: return "odd"


number = int(input("Please enter a number: "))
print("The number is", number_classifier(number), "and", check_odd_even(number)+".")

