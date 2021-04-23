
# print(“\033[H\033[J”)
# for i in [1,2,3,5,6,7]:

#     print(i).

# seasons=('spring', 'summer','autumn')
# for test in    seasons :
#     print("the season in row is", test)
# print("this line how many time will be repeated, depent of the positiom of print will see big difference")
# names=['ahmed', "mohamed", 'Aicha']
# for name in names:
#     print ("hello",   name)
#     print ("hello {}".format(name))
#     print (f"hello name")
# our_list=[]
# for i in range(1,6 ):
#     our_list.append(i)
# print(our_list)
# our_tuple=tuple(our_list)
# print(our_tuple)

# course ="abbi"
# for i in course:
#     print (i ,end='-')
# user_input=input('please enter a word: ')
# counter=0
# for char in user_input:
#     course +=1
#     print("counter :" )
# print (user_input)

import os
def clear(): return os.system('cls')


clear()
usr={'a':15,'b':215,"m":3.2}
for key, value in usr.items():
    print(key,":",value)

# times =int(input("how many time you want me to say 'I love you': "))
# print  ("I will print 'I love you' ", times, "times")
# for i in range(times):
#     print  ("I love you")


# number = int(input('please enter a number between 1-10: '))
# for i in range(number):
#     print(i ," x ",number,'=',i*number)

# print(number)

# set_1=set(range(0,10))
# print(set_1)

# print(*range(25,5,-2)) check this out is very important

# text=['one','two','three','four']
# numbers=[1,2,3,4,5]
# for x,y in zip(text,numbers):
#     print(x,':',y)