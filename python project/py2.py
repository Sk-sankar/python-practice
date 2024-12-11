import random

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]

    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
        if user_choice == 'exit':
            print("Thanks for playing!")
            break
        if user_choice not in options:
            print("Invalid choice. Try again.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

rock_paper_scissors()


# from flask import Flask, render_template, request
# import random

# app = Flask(__name__)

# @app.route("/", methods=["GET"])
# def index():
#     return render_template("index.html", computer_choice="", result="")

# @app.route("/play", methods=["POST"])
# def play():
#     user_choice = request.form.get("choice")
#     options = ["rock", "paper", "scissors"]
#     computer_choice = random.choice(options)

#     if user_choice == computer_choice:
#         result = "It's a tie!"
#     elif (user_choice == "rock" and computer_choice == "scissors") or \
#          (user_choice == "paper" and computer_choice == "rock") or \
#          (user_choice == "scissors" and computer_choice == "paper"):
#         result = "You win!"
#     else:
#         result = "You lose!"

#     return render_template("index.html", computer_choice=computer_choice, result=result)

# if __name__ == "__main__":
#     app.run(debug=True)