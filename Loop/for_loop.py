# for loop are used wwhen you have a block of cide which you want to repeat a fixed number of times

# food=['dosa','momo','biriyani','rice']
# for i in food:
#     print(i)

# range (sart,stop,step)-> number of Sequence
# start by default
# stop(excluded)
# step(by default 1)

# for i in range(10):
#     print(i)

# for i in range(2,10):
#     print(i)

# for i in range(2,10,2):
#     print(i)

for i in range(10,4,-2):
    print(i)

food=['dosa','momo','biriyani','rice'] 
for i in range(len(food)):
    print(food[i],'-',i)