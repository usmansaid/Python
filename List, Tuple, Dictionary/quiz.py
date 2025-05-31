quiz = [
    {
        "Question" : "What is the language mostly used in web development?",
        "Options" : ("Java", "Python", "HTML", "None"),
        "Correct" : "HTML"
    },

    {
        "Question" : "The correct looping statement?",
        "Options" : ("if", "for", "else", "elif"),
        "Correct" : "for"
    },

    {
        "Question" : "The machine level language is?",
        "Options" : ("Java", "JavaScript", "Python", "Assembly"),
        "Correct" : "Assembly"
    }
]

score = 0

for Q in quiz:
    print(Q["Question"])
    for i, option in enumerate(Q["Options"], start = 1):
        print(f"{i}. {option}")

    userInput = int(input("Enter option number: "))
    choice = Q["Options"][userInput - 1]

    if choice == Q["Correct"]:
        print("Correct ✔")
        score += 1
    else:
        print("Incorrect ❌, the answer is", Q["Correct"])

print(f"Your score is {score} / {len(quiz)}")    


