list_b=list(range(1,101))
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("fzzBuzz")
    elif i%3 ==0:
        print("buzz")
    elif i%5 ==0:
        print("fzzz")
    else:
        print("none")
