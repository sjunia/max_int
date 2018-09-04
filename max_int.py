#1. taka inn tölu
#2. geyma hana sem núverandi hæstu tölu
#3. Þegar ný tala kemur inn berum saman við núverandi hæstu tölu.
#4. Hærri talan af þessum í skrefi 3. er geymd sem núverandi hæsta tala.
#4. Forritið á að enda þegar neikvæð tala kemur.

num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0


while num_int >= 0:
    num_int = int(input("Input a number: "))
    if num_int > max_int:
        max_int = num_int
    else:
        continue
print("The maximum is", max_int)    # Do not change this line

