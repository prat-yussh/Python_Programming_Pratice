import random

dict={
    -1:"Rock",
    0:"Paper",
    1:"Scesor"
}

random_number = random.choice([-1, 0, 1])
computr = dict[random_number]

print(computr)