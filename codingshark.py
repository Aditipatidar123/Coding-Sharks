# import streamlit as st
# import pandas as pd
# import os

# # Set up page configuration
# st.set_page_config(page_title="Python Kids Test", layout="centered")

# # Sidebar menu
# menu = st.sidebar.selectbox("Select Page", ["Home", "Register", "Test", "Result", "Participants"])

# # Path to store results
# data_file = "participants.csv"

# # Load or create DataFrame
# if os.path.exists(data_file):
#     df = pd.read_csv(data_file)
# else:
#     df = pd.DataFrame(columns=["Name", "Roll Number", "School", "Score"])

# # Sample questions (20: mixed MCQ + code)
# questions = [
#     {
#         "question": "What is the output of: print(2 + 3 * 2)?",
#         "type": "mcq",
#         "options": ["10", "8", "7", "12"],
#         "answer": "8"
#     },
#     {
#         "question": "Write code to print numbers from 1 to 5 using a for loop.",
#         "type": "code",
#         "answer": "for i in range(1, 6):\n    print(i)"
#     },
#     {
#         "question": "What keyword is used to define a function in Python?",
#         "type": "mcq",
#         "options": ["func", "def", "function", "define"],
#         "answer": "def"
#     },
#     {
#         "question": "Write a function to return the square of a number.",
#         "type": "code",
#         "answer": "def square(n):\n    return n * n"
#     },
#     {
#         "question": "Which data type is used to store multiple values in a single variable?",
#         "type": "mcq",
#         "options": ["int", "str", "list", "bool"],
#         "answer": "list"
#     },
#     {
#         "question": "Write code to check if a number is even or odd.",
#         "type": "code",
#         "answer": "num = 4\nif num % 2 == 0:\n    print(\"Even\")\nelse:\n    print(\"Odd\")"
#     },
#     {
#         "question": "What is the correct way to start an if statement in Python?",
#         "type": "mcq",
#         "options": ["if x > 0 then:", "if (x > 0)", "if x > 0:", "if x > 0"],
#         "answer": "if x > 0:"
#     },
#     {
#         "question": "Write a list with elements 'apple', 'banana', 'cherry' and print it.",
#         "type": "code",
#         "answer": "fruits = ['apple', 'banana', 'cherry']\nprint(fruits)"
#     },
#     {
#         "question": "Which of the following is a dictionary?",
#         "type": "mcq",
#         "options": ["[1, 2, 3]", "(1, 2, 3)", "{1: 'one', 2: 'two'}", "{1, 2, 3}"],
#         "answer": "{1: 'one', 2: 'two'}"
#     },
#     {
#         "question": "Write code to create a dictionary of a student with name and age.",
#         "type": "code",
#         "answer": "student = {'name': 'John', 'age': 12}\nprint(student)"
#     },
#     {
#         "question": "What will print(len('Python')) output?",
#         "type": "mcq",
#         "options": ["6", "5", "7", "Error"],
#         "answer": "6"
#     },
#     {
#         "question": "Write a loop to print even numbers from 2 to 10.",
#         "type": "code",
#         "answer": "for i in range(2, 11, 2):\n    print(i)"
#     },
#     {
#         "question": "Which keyword is used to start a loop in Python?",
#         "type": "mcq",
#         "options": ["for", "loop", "iterate", "run"],
#         "answer": "for"
#     },
#     {
#         "question": "Write code to calculate the sum of numbers in a list.",
#         "type": "code",
#         "answer": "numbers = [1, 2, 3]\ntotal = sum(numbers)\nprint(total)"
#     },
#     {
#         "question": "Which symbol is used to comment in Python?",
#         "type": "mcq",
#         "options": ["//", "--", "#", "/* */"],
#         "answer": "#"
#     },
#     {
#         "question": "Write a function that returns True if a number is positive.",
#         "type": "code",
#         "answer": "def is_positive(n):\n    return n > 0"
#     },
#     {
#         "question": "What is the type of: type(123)?",
#         "type": "mcq",
#         "options": ["str", "type", "int", "float"],
#         "answer": "type"
#     },
#     {
#         "question": "Write code to reverse a string in Python.",
#         "type": "code",
#         "answer": "s = 'hello'\nprint(s[::-1])"
#     },
#     {
#         "question": "Which of the following is used to define a string?",
#         "type": "mcq",
#         "options": ["{}", "[]", "'' or \"\"", "()"],
#         "answer": "'' or \"\""
#     },
#     {
#         "question": "Write code to multiply two numbers input by the user.",
#         "type": "code",
#         "answer": "a = int(input())\nb = int(input())\nprint(a * b)"
#     }
# ]

# # Initialize session state
# for key in ["score", "submitted", "name", "roll", "school"]:
#     if key not in st.session_state:
#         st.session_state[key] = "" if key in ["name", "roll", "school"] else 0

# # Page logic
# if menu == "Home":
#     st.title("Welcome to coding shark Python Test Portal 🐍")
#     st.write("Test your knowledge of Python basics including If-Else, Loops, Functions, Lists and Dictionaries!")

# elif menu == "Register":
#     st.title("📝 Registration Form")
#     st.session_state.name = st.text_input("Enter your name")
#     st.session_state.roll = st.text_input("Enter your roll number")
#     st.session_state.school = st.text_input("Enter your school name")
#     if st.button("Register"):
#         st.success("Registration successful! Now go to the 'Test' page.")

# elif menu == "Test":
#     if not st.session_state.name or not st.session_state.roll:
#         st.warning("Please complete registration first.")
#     else:
#         st.title("🚀 Python Basics Test")
#         score = 0
#         answers = []

#         for idx, q in enumerate(questions):
#             st.subheader(f"Q{idx+1}. {q['question']}")
#             if q['type'] == 'mcq':
#                 ans = st.radio("Choose an option:", q['options'], key=idx)
#             elif q['type'] == 'code':
#                 ans = st.text_area("Write your Python code:", key=idx)
#             answers.append(ans)

#         if st.button("Submit Test"):
#             for idx, q in enumerate(questions):
#                 user_ans = answers[idx].strip()
#                 correct_ans = q['answer'].strip()
#                 if q['type'] == 'mcq' and user_ans == correct_ans:
#                     score += 1
#                 elif q['type'] == 'code' and user_ans.replace(' ', '') == correct_ans.replace(' ', ''):
#                     score += 1
#             st.session_state.score = score
#             st.session_state.submitted = True
#             st.success(f"Test Submitted! You scored {score} out of {len(questions)}.")

#             new_data = pd.DataFrame([{
#                 "Name": st.session_state.name,
#                 "Roll Number": st.session_state.roll,
#                 "school": st.session_state.school,
#                 "Score": score
#             }])
#             df = pd.concat([df, new_data], ignore_index=True)
#             df.to_csv(data_file, index=False)

# elif menu == "Result":
#     st.title("📊 Test Result")
#     if st.session_state.submitted:
#         st.write(f"Your score is: {st.session_state.score} / {len(questions)}")
#         if st.session_state.score == len(questions):
#             st.success("Excellent! 🏆")
#         elif st.session_state.score >= len(questions) // 2:
#             st.info("Good Job! Keep practicing. 💪")
#         else:
#             st.warning("Don't worry, try again! Practice makes perfect. 🤗")
#     else:
#         st.write("Please take the test first.")

# elif menu == "Participants":
#     st.title("👥 Participants")
#     if df.empty:
#         st.info("No participants yet.")
#     else:
#         st.dataframe(df)
# import streamlit as st
# import pandas as pd
# from datetime import datetime
# import os

# # Set up page configuration
# st.set_page_config(page_title="Python Kids Test", layout="centered")

# # Sidebar menu
# menu = st.sidebar.selectbox("Select Page", ["Home", "Register", "Test", "Result", "Participants"])

# # Sample questions (Mixed: MCQ + Coding)
# questions = [
#     {"question": "What is the output of: print(2 + 3 * 2)?", "type": "mcq", "options": ["10", "8", "7", "12"], "answer": "8"},
#     {"question": "Write code to print numbers from 1 to 5 using a for loop.", "type": "code", "answer": "for i in range(1, 6):\n    print(i)"},
#     {"question": "What keyword is used to define a function in Python?", "type": "mcq", "options": ["func", "def", "function", "define"], "answer": "def"},
#     {"question": "Write a function to return the square of a number.", "type": "code", "answer": "def square(n):\n    return n * n"},
#     {"question": "Which data type is used to store multiple values in a single variable?", "type": "mcq", "options": ["int", "str", "list", "bool"], "answer": "list"},
#     {"question": "Write code to check if a number is even or odd.", "type": "code", "answer": "num = 4\nif num % 2 == 0:\n    print(\"Even\")\nelse:\n    print(\"Odd\")"},
#     {"question": "What is the correct way to start an if statement in Python?", "type": "mcq", "options": ["if x > 0 then:", "if (x > 0)", "if x > 0:", "if x > 0"], "answer": "if x > 0:"},
#     {"question": "Write a list with elements 'apple', 'banana', 'cherry' and print it.", "type": "code", "answer": "fruits = ['apple', 'banana', 'cherry']\nprint(fruits)"},
#     {"question": "Which of the following is a dictionary?", "type": "mcq", "options": ["[1, 2, 3]", "(1, 2, 3)", "{1: 'one', 2: 'two'}", "{1, 2, 3}"], "answer": "{1: 'one', 2: 'two'}"},
#     {"question": "Write code to create a dictionary of a student with name and age.", "type": "code", "answer": "student = {'name': 'John', 'age': 12}\nprint(student)"}
# ]

# # Store results and registration info
# if 'score' not in st.session_state:
#     st.session_state.score = 0
# if 'submitted' not in st.session_state:
#     st.session_state.submitted = False
# if 'registered' not in st.session_state:
#     st.session_state.registered = False

# # Home Page
# if menu == "Home":
#     st.title("Welcome to Python Test Portal 🐍")
#     st.write("Test your knowledge of Python basics including If-Else, Loops, Functions, Lists and Dictionaries!")

# # Register Page
# elif menu == "Register":
#     st.title("📝 Registration Form")
#     name = st.text_input("Enter your name")
#     roll = st.text_input("Enter your roll number")
#     school = st.text_input("Enter your school name")

#     if st.button("Done"):
#         if name and roll and school:
#             # Check for duplicate roll number
#             if os.path.exists("student_data.csv"):
#                 existing_data = pd.read_csv("student_data.csv")
#                 if roll in existing_data['Roll No'].astype(str).values:
#                     st.error("This roll number is already registered.")
#                 else:
#                     st.session_state.name = name
#                     st.session_state.roll = roll
#                     st.session_state.school = school
#                     st.session_state.registered = True
#                     st.success("You're registered and ready to take the test!")
#             else:
#                 st.session_state.name = name
#                 st.session_state.roll = roll
#                 st.session_state.school = school
#                 st.session_state.registered = True
#                 st.success("You're registered and ready to take the test!")
#         else:
#             st.warning("Please fill all fields.")

# # Test Page
# elif menu == "Test":
#     if not st.session_state.registered:
#         st.warning("Please register first before taking the test.")
#     else:
#         st.title("🚀 Python Basics Test")
#         score = 0
#         answers = []

#         for idx, q in enumerate(questions):
#             st.subheader(f"Q{idx+1}. {q['question']}")
#             if q['type'] == 'mcq':
#                 ans = st.radio("Choose an option:", q['options'], key=idx)
#             elif q['type'] == 'code':
#                 ans = st.text_area("Write your Python code:", key=idx)
#             answers.append(ans)

#         if st.button("Submit Test"):
#             for idx, q in enumerate(questions):
#                 user_ans = answers[idx].strip()
#                 correct_ans = q['answer'].strip()
#                 if q['type'] == 'mcq' and user_ans == correct_ans:
#                     score += 1
#                 elif q['type'] == 'code' and user_ans.replace(' ', '') == correct_ans.replace(' ', ''):
#                     score += 1

#             st.session_state.score = score
#             st.session_state.submitted = True
#             st.success(f"Test Submitted! You scored {score} out of {len(questions)}.")

#             # Save result to CSV
#             student_data = {
#                 "Name": st.session_state.name,
#                 "Roll No": st.session_state.roll,
#                 "School": st.session_state.school,
#                 "Score": score,
#                 "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             }

#             file_exists = os.path.isfile("student_data.csv")
#             df = pd.DataFrame([student_data])

#             if file_exists:
#                 df.to_csv("student_data.csv", mode='a', index=False, header=False)
#             else:
#                 df.to_csv("student_data.csv", index=False)

# # Result Page
# elif menu == "Result":
#     st.title("📊 Test Result")
#     if st.session_state.submitted:
#         st.write(f"Your score is: {st.session_state.score} / {len(questions)}")
#         if st.session_state.score == len(questions):
#             st.success("Excellent! 🏆")
#         elif st.session_state.score >= len(questions) // 2:
#             st.info("Good Job! Keep practicing. 💪")
#         else:
#             st.warning("Don't worry, try again! Practice makes perfect. 🤗")
#     else:
#         st.write("Please take the test first.")

# # Participants Page
# elif menu == "Participants":
#     st.title("👥 List of Participants")
#     if os.path.exists("student_data.csv"):
#         df = pd.read_csv("student_data.csv")
#         st.dataframe(df.drop_duplicates(subset=["Roll No"]))
#     else:
#         st.info("No participants yet.")
import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Set up page configuration
st.set_page_config(page_title="Python Kids Test", layout="centered")

# Sidebar menu
menu = st.sidebar.selectbox("Select Page", ["Home", "Register", "Test", "Result", "Participants"])

# Sample questions (Extended to 20)
questions = [
    {"question": "What is the output of: print(2 + 3 * 2)?", "type": "mcq", "options": ["10", "8", "7", "12"], "answer": "8"},
    {"question": "Write code to print numbers from 1 to 5 using a for loop.", "type": "code", "answer": "for i in range(1, 6):\n    print(i)"},
    {"question": "What keyword is used to define a function in Python?", "type": "mcq", "options": ["func", "def", "function", "define"], "answer": "def"},
    {"question": "Write a function to return the square of a number.", "type": "code", "answer": "def square(n):\n    return n * n"},
    {"question": "Which data type is used to store multiple values in a single variable?", "type": "mcq", "options": ["int", "str", "list", "bool"], "answer": "list"},
    {"question": "Write code to check if a number is even or odd.", "type": "code", "answer": "num = 4\nif num % 2 == 0:\n    print(\"Even\")\nelse:\n    print(\"Odd\")"},
    {"question": "What is the correct way to start an if statement in Python?", "type": "mcq", "options": ["if x > 0 then:", "if (x > 0)", "if x > 0:", "if x > 0"], "answer": "if x > 0:"},
    {"question": "Write a list with elements 'apple', 'banana', 'cherry' and print it.", "type": "code", "answer": "fruits = ['apple', 'banana', 'cherry']\nprint(fruits)"},
    {"question": "Which of the following is a dictionary?", "type": "mcq", "options": ["[1, 2, 3]", "(1, 2, 3)", "{1: 'one', 2: 'two'}", "{1, 2, 3}"], "answer": "{1: 'one', 2: 'two'}"},
    {"question": "Write code to create a dictionary of a student with name and age.", "type": "code", "answer": "student = {'name': 'John', 'age': 12}\nprint(student)"},
    {"question": "Which loop is used when the number of iterations is known?", "type": "mcq", "options": ["while", "do-while", "for", "loop"], "answer": "for"},
    {"question": "Write code to print even numbers from 1 to 10.", "type": "code", "answer": "for i in range(1, 11):\n    if i % 2 == 0:\n        print(i)"},
    {"question": "Which keyword is used to create a loop in Python?", "type": "mcq", "options": ["loop", "iterate", "for", "repeat"], "answer": "for"},
    {"question": "Write a function to return the sum of two numbers.", "type": "code", "answer": "def add(a, b):\n    return a + b"},
    {"question": "Which keyword is used to exit a loop?", "type": "mcq", "options": ["stop", "exit", "break", "terminate"], "answer": "break"},
    {"question": "Write code to count from 10 to 1.", "type": "code", "answer": "for i in range(10, 0, -1):\n    print(i)"},
    {"question": "Which of the following is a valid list in Python?", "type": "mcq", "options": ["{1,2,3}", "[1,2,3]", "(1,2,3)", "<1,2,3>"], "answer": "[1,2,3]"},
    {"question": "Write code to add a new key 'grade' to a student dictionary.", "type": "code", "answer": "student = {'name': 'John'}\nstudent['grade'] = 'A'\nprint(student)"},
    {"question": "Which data structure is used for key-value pairs?", "type": "mcq", "options": ["list", "tuple", "set", "dictionary"], "answer": "dictionary"},
    {"question": "Write code to get the length of a list.", "type": "code", "answer": "my_list = [1, 2, 3, 4]\nprint(len(my_list))"}
]

# Store results and registration info
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'registered' not in st.session_state:
    st.session_state.registered = False

# Home Page
if menu == "Home":
    st.title("Welcome to Python Test Portal 🐍")
    st.write("Test your knowledge of Python basics including If-Else, Loops, Functions, Lists and Dictionaries!")

# Register Page
elif menu == "Register":
    st.title("📝 Registration Form")
    name = st.text_input("Enter your name")
    roll = st.text_input("Enter your roll number")
    school = st.text_input("Enter your school name")

    if st.button("Done"):
        if name and roll and school:
            # Check for duplicate roll number
            if os.path.exists("student_data.csv"):
                existing_data = pd.read_csv("student_data.csv")
                if roll in existing_data['Roll No'].astype(str).values:
                    st.error("This roll number is already registered.")
                else:
                    st.session_state.name = name
                    st.session_state.roll = roll
                    st.session_state.school = school
                    st.session_state.registered = True
                    st.success("You're registered and ready to take the test!")
            else:
                st.session_state.name = name
                st.session_state.roll = roll
                st.session_state.school = school
                st.session_state.registered = True
                st.success("You're registered and ready to take the test!")
        else:
            st.warning("Please fill all fields.")

# Test Page
elif menu == "Test":
    if not st.session_state.registered:
        st.warning("Please register first before taking the test.")
    else:
        st.title("🚀 Python Basics Test")
        score = 0
        answers = []

        for idx, q in enumerate(questions):
            st.subheader(f"Q{idx+1}. {q['question']}")
            if q['type'] == 'mcq':
                ans = st.radio("Choose an option:", q['options'], key=idx)
            elif q['type'] == 'code':
                ans = st.text_area("Write your Python code:", key=idx)
            answers.append(ans)

        if st.button("Submit Test"):
            for idx, q in enumerate(questions):
                user_ans = answers[idx].strip()
                correct_ans = q['answer'].strip()
                if q['type'] == 'mcq' and user_ans == correct_ans:
                    score += 1
                elif q['type'] == 'code' and user_ans.replace(' ', '') == correct_ans.replace(' ', ''):
                    score += 1

            st.session_state.score = score
            st.session_state.submitted = True
            st.success(f"Test Submitted! You scored {score} out of {len(questions)}.")

            # Save result to CSV
            student_data = {
                "Name": st.session_state.name,
                "Roll No": st.session_state.roll,
                "School": st.session_state.school,
                "Score": score,
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            file_exists = os.path.isfile("student_data.csv")
            df = pd.DataFrame([student_data])

            if file_exists:
                df.to_csv("student_data.csv", mode='a', index=False, header=False)
            else:
                df.to_csv("student_data.csv", index=False)

# Result Page
elif menu == "Result":
    st.title("📊 Test Result")
    if st.session_state.submitted:
        st.write(f"Your score is: {st.session_state.score} / {len(questions)}")
        if st.session_state.score == len(questions):
            st.success("Excellent! 🏆")
        elif st.session_state.score >= len(questions) // 2:
            st.info("Good Job! Keep practicing. 💪")
        else:
            st.warning("Don't worry, try again! Practice makes perfect. 🤗")
    else:
        st.write("Please take the test first.")

# Participants Page
elif menu == "Participants":
    st.title("👥 List of Participants")
    if os.path.exists("student_data.csv"):
        df = pd.read_csv("student_data.csv")
        st.dataframe(df.drop_duplicates(subset=["Roll No"]))
    else:
        st.info("No participants yet.")

