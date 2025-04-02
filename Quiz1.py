#!/usr/bin/env python3
# Quiz1.py - Animal Quiz Game
# Author: [Your Name]
# Date: [Current Date]
# Description: A simple animal quiz game that checks answers and calculates score

def quiz():
    print("Welcome to the Animal Quiz!")
    print("Answer the following questions:\n")

    # Questions and Answers
    questions = [
        "1. What is the largest animal on Earth?:\n   a. Blue Whale\n   b. Mouse\n   c. Cat",
        "2. Which bird can fly backwards?:\n   a. Cuckoo\n   b. Eagle\n   c. Hummingbird",
        "3. What is the only mammal capable of flight?:\n   a. Bat\n   b. Squirrel\n   c. Dolphin"
    ]
    
    answers = ["a", "c", "a"]  # Correct answer letters
    score = 0

    # Ask questions
    for i in range(len(questions)):
        print(questions[i])
        user_answer = input("Your answer (a/b/c): ").strip().lower()
        
        if user_answer == answers[i]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {answers[i]}.\n")

    # Provide final score
    print("\nQuiz completed!")
    print(f"You got {score} out of {len(questions)} questions correct.")

# Run the quiz
if __name__ == "__main__":
    quiz()
