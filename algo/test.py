diff = int(input())

if diff >= 1 and diff <= 9:
    print("easy")
elif diff >= 11 and diff <= 19:
    print("normal")
elif diff >= 21 and diff <= 29:
    print("hard")
elif diff == 10 or diff == 20 or diff == 30:
    print("special")
else:
    pass
