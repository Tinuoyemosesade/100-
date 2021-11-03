# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
result = name1 + name2
love_message = ""
count_1 = 0
count_2 = 0

for letter in result:
    if letter.lower() in "true":
        count_1 += 1
    if letter.lower() in "love":
        count_2 += 1

    result = int(str(count_1) + str(count_2))

if result < 10 or result > 90:
    love_message = ", you go together like coke and mentos."
if 40 < result < 50:
    love_message = ", you are alright together."
else:
    love_message = "."

print(f"Your score is {result}{love_message}")