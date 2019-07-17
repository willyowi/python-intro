
# for number in numbers:
#     print(number)

# list_a=list(range(50,66))
# print(list_a)
# for i in range(0,7):
#     print("I would love " + str(i) + " cookies")
# for i in range(1,7):
#      print("I would love "+str(i)+" cookies")


######fzzzBuzzz
# numbers=[1,2,3,4,5,6]
# for i in numbers:
#     if i %2==0:
#         print(str(i)+" buzz")
#     elif i%2==1:
#         print(str(i)+" fsss")
# /////////////////////////////magic 8
#import sys
# import random
# ans="True"
# while ans=="True":
#     random=random.randint(1,10)
#
#     if random==1:
#         print("wow,yea")
#     elif random==2:
#         print("not really")
#     else:
#         print("talk again")

   #qst=input()
# print(random.randint(1,11))
# qst=input()
# for random.randint:
#     if  random.randint==1
#     print("yes")
# else:
#     print ("no")

#if random.randint==1:
#    print("as I see,Yes")
#else:
#    print("no")


# elif ram==3:
#    print("Ask me again Later")
# elif ram==4:
#    print("Dont count on it")
# elif ram==5:
#    print(" It is decidedly so.")
# elif ram==6:
#    print("Cannot predict now")
# elif ram==7:
#    print("Better not tell you now.")
# elif ram==8:
#    print("Yes")
# elif ram==9:
#    print("most likely,Yes")
# elif ram==10:
#    print("acha ujinga unanisumbua")
 #else:
    #print("kwenda unaboo")

    #############the real functioning one
from random import randint
ans1 ="maybe"
ans3 ="yes"
ans2 = "Ata me sijui"
ans4 ="no"
ans5 ="Just be Patient"
ans6 ="well i dont think so"
ans7 ="ofcos"
ans8 ="nop nop"

name = input("Enter your name:")
input(name + ",Whats your question?")

choice = randint(1,7)
if choice == 1:
    answer = ans1
elif choice == 2:
    answer = ans5
elif choice == 3:
    answer = ans4
elif choice == 4:
    answer = ans3
elif choice == 5:
    answer = ans6
elif choice == 6:
    answer = ans7
elif choice == 7:
    answer = ans2
else:
    answer = ans8
print( "The fairy teller says:" + answer)
