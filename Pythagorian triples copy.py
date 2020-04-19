import math
f = open("900,000,000 Pythagorian Triples.txt","w")
count = int(input("ah oh"))
for i in range(int(input("How high would you like this to go?"))):
    whiind = 1
    while whiind<i:
        count -= 1
        if math.gcd(2*i*whiind,i**2-whiind**2) == 1:
            f.write(str(2*i*whiind)+", "+str(i**2-whiind**2)+", "+str(i**2+whiind**2)+"\n")
        whiind += 1
        if count == 0:
            break
f.close()
print("Done")
