import random
while True:
    text = input("> ")
    a = ['HI','Hello']
    b = ['Hello :D','Hi',':D']
    if text in a:
        print(random.choice(b))
    else:
        print("?")
