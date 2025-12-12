# ---------------------------------------------------QUIZ GAME IN PYTHON---------------------------------------------------
# time library
import time

total_questions = 5

# welcome screen page
print("*" * 100)
project_name = "🎯 WELCOME TO THE QUIZ GAME🎯 "
print(project_name.center(100))
print("*" * 100)
time.sleep(1)

# check you are interested or not
print("Hello! Are you ready to play Quiz Game? (yes/no)")
user_input = input("Enter your answer: ")
if user_input.lower() == "yes":
    print("Great👍 Let's start the game!")  # your game code will start here
else:
    print("Alright 🙂 See you next time!")

# Take user information
print("\nPlease Enter your Details:\n")
name = input("👉 Enter Your Name: ")
mobile = input("👉 Enter Your Mobile Number: ")
date_of_birth = input("👉 Enter Your Date of Birth (dd/mm/yyyy): ")

print("\nThank You! Your details are saved ✅")
print(f"Name: {name}\nMobile: {mobile}\nDOB: {date_of_birth}")
print("=" * 100)
time.sleep(1)

# game start
print("\n📚 Please Select a Topic to Start the Quiz:")
print("1. Python")
print("2. Maths")
print("3. Sports")
print("4. Geography")

# Choose the subject
Subject = input("\n👉 Choose a topic (1/2/3/4): ")

score = 0

# -------------------------PYTHON-------------------------
if Subject == "1":
    print("\n💻 You selected Python\n")

#que1
    
    Que = input("""1). What is the variable in python?

a) A reserved word 
b) A data type 
c) A location in memory to store data 
d) A function 
👉 answer: """).lower()

    if Que == "c" or Que == "a location in memory to store data":
        print("✅ this answer is correct.\n")
        score += 1
    else:
        print("❌ Wrong!  \n✔ correct answer: A location in memory to store data\n")

#que2
        
    Que = input("""2). Which of the following data types is immutable in python?

a) List 
b) Tuple
c) Set
d) Dictionary
👉 answer: """).lower()

    if Que == "b" or Que == "tuple":
        print("✅ this answer is correct.\n")
        score += 1
    else:
        print("❌ Wrong!  \n✔ correct answer: Tuple\n")

#que3
        
    Que = input("""3). What is an exception in python?

a) A runtime error 
b) A logical error
c) A syntax error
d) A compile-time error
👉 answer: """).lower()

    if Que == "a" or Que == "a runtime error":
        print("✅ this answer is correct.\n")
        score += 1
    else:
        print("❌ Wrong!  \n✔ correct answer: A runtime error\n")

#que4
        
    Que = input("""4). What is called when a function is defined inside a class?

a) Module 
b) Class
c) Another function
d) Method
👉 answer: """).lower()

    if Que == "d" or Que == "method":
        print("✅ this answer is correct.\n")
        score += 1
    else:
        print("❌ Wrong!  \n✔ correct answer: Method\n")

#que5
        
    Que = input("""5). Who developed Python Programming Language?

a) Wick van Rossum.
b) Rasmus Lerdorf.
c) Guido van Rossum.
d) Niene Stom.
👉 answer: """).lower()

    if Que == "c" or Que == "Guido van Rossum.":
        print("✅ this answer is correct.\n")
        score += 1
    else:
        print("❌ Wrong!  \n✔ correct answer: Guido van Rossum.\n")


# -------------------------MATHS-------------------------
elif Subject == "2":
    print("\n🔢 You selected Maths\n")

#que1
    
    Que = input("""1). What is the product of 12 and 12?

a) 144
b) 124
c) 134
d) 154
👉 answer: """).lower()

    if Que == "a" or Que == "144":
        print("✅ this answer is correct.\n")
        score += 1
    else:
        print("❌ Wrong!  \n✔ correct answer: 144\n")

#que2
        
    Que = input("""2). What is the value of 2 the power of 5?

a) 10
b) 32
c) 25
d) 16
👉 answer: """).lower()

    if Que == "b" or Que == "32":
        print("✅ this answer is correct.\n")
        score += 1
    else:
        print("❌ Wrong!  \n✔ correct answer: 32\n")

#que3
        
    Que = input("""3). What is the average of 10, 20 and 30?

a) 20
b) 25
c) 15
d) 30
👉 answer: """).lower()

    if Que == "a" or Que == "20":
        print("✅ this answer is correct.\n")
        score += 1
    else:
        print("❌ Wrong!  \n✔ correct answer: 20\n")

#que4
        
    Que = input("""4). What is the largest two-digit prime number?

a) 93
b) 87
c) 91
d) 97
👉 answer: """).lower()

    if Que == "d" or Que == "97":
        print("✅ this answer is correct.\n")
        score += 1
    else:
        print("❌ Wrong!  \n✔ correct answer: 97\n")

#que5
        
    Que = input("""5). What is the sum of 555 + 555 + 123?

a) 1103.
b) 1223.
c) 1233.
d) 1123.
👉 answer: """).lower()

    if Que == "c" or Que == "1233":
        print("✅ this answer is correct.\n")
        score += 1
    else:
        print("❌ Wrong!  \n✔ correct answer: 1233\n")

# -------------------------SPORTS-------------------------

elif Subject == "3":
    print("\n⚽ You selected Sports\n")

#que1
    
    Que = input("""1). Which of the following is the highest award in sports in the world?

a) Mrgaret thather award.
b) Laureus world sports award.
c) Olympic order.
d) jesse owens award.
👉 answer: """).lower()

    if Que == "c" or Que == "Olympic order":
        print("✅ this answer is correct.\n")
        score += 1
    else:
        print("❌ Wrong!  \n✔ correct answer: Olympic order\n")

#que2
        
    Que = input("""2). India won its first and last olympic hockey gold in...?

a) 1926 and 1982.
b) 1928 and 1980.
c) 1936 and 1984.
d) 1947 and 1992.
👉 answer: """).lower()

    if Que == "b" or Que == "1928 and 1980":
        print("✅ this answer is correct.\n")
        score += 1
    else:
        print("❌ Wrong!  \n✔ correct answer: 1928 and 1980\n")
#que3
        
    Que = input("""3).Number of players in a team of watSer polo is?

a) 5
b) 6
c) 8
d) 7
👉 answer: """).lower()

    if Que == "d" or Que == "7":
        print("✅ this answer is correct.\n")
        score += 1
    else:
        print("❌ Wrong!  \n✔ correct answer: 7\n")
        
#que4
        
    Que = input("""4).Which country hosts the inaugural kho kho world cup in 2025?)

a) Nepal.
b) China.
c) India.
d) Bhutan.
👉 answer: """).lower()

    if Que == "c" or Que == "India":
        print("✅ this answer is correct.\n")
        score += 1
    else:
        print("❌ Wrong!  \n✔ correct answer: India\n")

#que5
        
    Que = input("""5).In which country, the first Youth Olympic Games was held?

a) Japan.
b) Singapore.
c) Vietnam.
d) South Korea.
    👉 answer: """).lower()

    if Que == "b" or Que == "Singapore.":
        print("✅ this answer is correct.\n")
        score += 1
    else:
        print("❌ Wrong!  \n✔ correct answer: Singapore.\n")


# -------------------------GEOGRAPHY-------------------------
elif Subject == "4":
    print("\n🌏 You selected Geography\n")

#que1
    
    Que = input("""1). Which among the following is a riverine (Inland River) port?

a) Chennai.
b) Tamil Nadu.
c) Maharashtra.
d) Kolkata.
👉 answer: """).lower()

    if Que == "d" or Que == "Kolkata":
        print("✅ this answer is correct.\n")
        score += 1
    else:
        print("❌ Wrong!  \n✔ correct answer: Kolkata\n")

#que2
        
    Que = input("""2). Which of the following rivers flows between Vindhya and Satpura ranges?

a) Narmada.
b) Godavari.
c) tapti.
d) Mahanadi.
👉 answer: """).lower()

    if Que == "a" or Que == "Narmada":
        print("✅ this answer is correct.\n")
        score += 1
    else:
        print("❌ Wrong! \n✔ correct answer: Narmada\n")

#que3
        
    Que = input("""3).The Baratang Island mangroves is located in which of the following places of India?


a) Odisha.
b) Andaman and Nicobar.
c) Lakhwadeep.
d) New Moore.
👉 answer: """).lower()

    if Que == "b" or Que == "Andaman and Nicobar.":
        print("✅ this answer is correct.\n")
        score += 1
    else:
        print("❌ Wrong! \n✔ correct answer: Andaman and Nicobar.\n")

#que4
        
    Que = input("""4).What percent of oil needs is imported by India?

a) 54%.
b) 67%.
c) 82%.
d) 95%.
👉 answer: """).lower()

    if Que == "c" or Que == "82%.":
        print("✅ this answer is correct.\n")
        score += 1
    else:
        print("❌ Wrong!  \n✔ correct answer: 82%.\n")

#que5
        
    Que = input("""5).When is National Nutrition Week observed in India?

a) 1–7 September.
b) 15–21 September.
c) 1–7 October.
d) 1–7 August.
👉 answer: """).lower()

    if Que == "a" or Que == "1–7 September.":
        print("✅ this answer is correct.\n")
        score += 1
    else:
        print("❌ Wrong!  \n✔ correct answer: 1–7 September.\n")

        
#scoring performance
        
def performance(score, total):
    percent = (score / total) * 100
    print("\n" + "-" * 50)
    print(f"✅ Your Final Score: {score}/{total}")
    print(f"📊 Percentage: {percent:.2f}%")

    if percent == 100:
        print("\nCongratulations 😍")
        print("Excellent! Perfect Score!🏆")
    elif percent >= 70:
        print("\nCongratulations 🙂")
        print("Great Job! Keep it up!🎉")
    elif percent >= 40:
        print("\nCongratulations 👍")
        print("Good Try! You can improve!🙂")
    else:
        print("Needs Improvement. Try Again!😢")
    print("-" * 50)

# ---------------- Final Result ----------------
performance(score, total_questions)

# last message
print("\nThank You for Playing the Quiz Game 😊😊😊")

