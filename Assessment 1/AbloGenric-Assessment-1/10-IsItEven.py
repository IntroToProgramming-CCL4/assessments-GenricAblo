def is_even_or_odd():
    x = int(input("Enter a number: "))
    if x % 2 == 0:
        return x, "is an even number"
    else:
        return x, "is not odd"

#print(is_even_or_odd())