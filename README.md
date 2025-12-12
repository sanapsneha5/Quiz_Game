# 🎯 Quiz Game in Python

A simple, fun, and interactive **command-line Quiz Game** built using Python.  
Users can choose from multiple topics such as **Python**, **Maths**, **Sports**, and **Geography**, answer multiple-choice questions, and receive a final score with performance feedback.

---

## 📘 Introduction

The **Quiz Game in Python** is perfect for beginners learning Python.  
It covers essential programming concepts such as:

- 📥 User Input & Output  
- 🔀 Conditional Statements  
- 🔁 Loops  
- ⏳ Time Delays using `time.sleep()`  

This project helps students practice Python while building a real-world application.

---

## ⭐ Features

✔️ Multiple quiz topics  
✔️ User detail input (name, age, etc.)  
✔️ 5 questions per quiz (customizable)  
✔️ Automatic score calculation  
✔️ Final performance summary  
✔️ Clean and beginner-friendly code  
✔️ Welcome screen with smooth delay effects  

---

## 📂 Project Structure

quiz-game/


├── quiz_game.py        # main quiz script (your code)

├── README.md           # this file



---

## 🛠️ Technologies Used

- **Python 3**
- Built-in Python modules:
  - `time`

---

## ▶️ How to Run the Game

1. **Install Python 3** on your system.

2. **Download or Clone the Repository**  
   ```bash
   git clone https://github.com/sanapsneha5/Quiz-Game.git
    ```

## Navigate to the Project Folder
```bash
   cd Quiz-Game
```

Run the Python File
```bash
python quiz.py
```

🧠 How the Quiz Works

1️⃣ Header and Imports
```bash
import time
```
time.sleep() is used to create smooth pauses in the quiz.


2️⃣ Welcome Screen

```bash
print("*" * 100)
project_name = "🎯 WELCOME TO THE QUIZ GAME🎯 "
print(project_name.center(100))
print("*" * 100)
time.sleep(1)
```
Displays a visually appealing banner.

3️⃣ Start Confirmation

```bash
user_input = input("Enter your answer: ")
if user_input.lower() == "yes":
```
Quiz starts only if the user enters yes.

4️⃣ User Details Input

```bash
name = input("👉 Enter Your Name: ")
mobile = input("👉 Enter Your Mobile Number: ")
date_of_birth = input("👉 Enter Your Date of Birth (dd/mm/yyyy): ")
```
The program stores the user's basic information.

5️⃣ Topic Selection

```bash
print("1. Python\n2. Maths\n3. Sports\n4. Geography")
Subject = input("\n👉 Choose a topic (1/2/3/4): ")
score = 0
```
User selects a topic from four categories.

6️⃣ Questions per Topic

Each topic contains 5 multiple-choice questions.

```bash
if Subject == "1":
    Que = input("""1). What is the variable in python?
a) A reserved word
b) A data type
c) A location in memory to store data
d) A function
👉 answer: """).lower()

    if Que == "c" or Que == "a location in memory to store data":
        score += 1
```
The answer can be entered as option letter (e.g., c) or as full text.

7️⃣ Performance Calculation

```bash
def performance(score, total):
    percent = (score / total) * 100
    print(f"✅ Your Final Score: {score}/{total}")
    print(f"📊 Percentage: {percent:.2f}%")
```
Displays final score, percentage, and performance feedback.

8️⃣ Exit Message

```bash
print("\nThank You for Playing the Quiz Game 😊😊😊")
Friendly closing note.
```
Friendly closing note.


🖥️ Sample Output

```bash
****************************************************************************************************
                                 🎯 WELCOME TO THE QUIZ GAME 🎯
****************************************************************************************************
Hello! Are you ready to play Quiz Game? (yes/no)
> yes
Great👍 Let's start the game!

Please Enter your Details:

👉 Enter Your Name: Sneha
👉 Enter Your Mobile Number: 9876543210
👉 Enter Your Date of Birth (dd/mm/yyyy): 01/01/2000

📚 Please Select a Topic:
1. Python
2. Maths
3. Sports
4. Geography
👉 Choose a topic (1/2/3/4): 1

1). What is the variable in python?
a) Reserved word
b) Data type
c) Location in memory to store data
d) Function
👉 answer: c
✅ this answer is correct.

--------------------------------------------------
✅ Your Final Score: 4/5
📊 Percentage: 80.00%

Congratulations 🙂
Great Job! Keep it up! 🎉
--------------------------------------------------

Thank You for Playing the Quiz Game 😊😊😊

```

▶️ How to Run

1.Install Python 3

2.Open terminal / command prompt

3.Run the script

```bash
python quiz_game.py
```

📄 License

This project is free to use for learning and educational purposes.



