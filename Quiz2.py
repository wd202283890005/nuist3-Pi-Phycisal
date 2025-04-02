#!/usr/bin/env python3
# Quiz2.py - Python Knowledge Quiz with LED Feedback
#Author : Di Wu
#Date : 2.4.2025
import RPi.GPIO as GPIO
import time

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GREEN_LED = 17  # GPIO17 for correct answers
RED_LED = 18    # GPIO18 for incorrect answers
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

def flash_led(pin, duration=0.5):
    """Flash an LED for visual feedback"""
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(pin, GPIO.LOW)

def quiz():
    print("\nWelcome to the Python Knowledge Quiz!")
    print("Answer with the letter (a/b/c/d/e) of the correct answer.\n")

    # Questions and Answers
    questions = [
        {
            "text": "1. Which of the following is NOT a python data type?\n"
                    "   a) int\n   b) float\n   c) rational\n   d) string\n   e) bool",
            "options": ['a', 'b', 'c', 'd', 'e'],
            "answer": 'c'
        },
        {
            "text": "2. Which of the following is NOT a built-in operation in Python?\n"
                    "   a) +\n   b) %\n   c) abs()\n   d) sqrt()",
            "options": ['a', 'b', 'c', 'd'],
            "answer": 'd'
        },
        {
            "text": "3. In a mixed-type expression involving ints and floats, Python will convert:\n"
                    "   a) floats to ints\n   b) ints to strings\n   c) floats and ints to strings\n   d) ints to floats",
            "options": ['a', 'b', 'c', 'd'],
            "answer": 'd'
        },
        {
            "text": "4. The best structure for implementing a multi-way decision in Python is:\n"
                    "   a) if\n   b) if-else\n   c) if-elif-else\n   d) try",
            "options": ['a', 'b', 'c', 'd'],
            "answer": 'c'
        },
        {
            "text": "5. What statement can be executed in the body of a loop to cause it to terminate?\n"
                    "   a) if\n   b) exit\n   c) continue\n   d) break",
            "options": ['a', 'b', 'c', 'd'],
            "answer": 'd'
        }
    ]
    
    score = 0

    try:
        # Ask questions
        for question in questions:
            print("\n" + "="*50)
            print(question["text"])
            while True:
                user_answer = input("Your choice (" + "/".join(question["options"]) + "): ").strip().lower()
                if user_answer in question["options"]:
                    break
                print("Invalid input! Please enter a valid option letter.")

            if user_answer == question["answer"]:
                print("\n✅ Correct!")
                flash_led(GREEN_LED)
                score += 1
            else:
                print(f"\n❌ Incorrect! The correct answer was {question['answer']}.")
                flash_led(RED_LED)

        # Quiz completion
        print("\n" + "="*50)
        print(f"\nQuiz completed! Your score: {score}/{len(questions)}")
        percentage = (score / len(questions)) * 100
        print(f"Percentage: {percentage:.1f}%")
        
        # Final LED feedback
        if percentage >= 60:
            flash_led(GREEN_LED, 1)
            flash_led(GREEN_LED, 1)
        else:
            flash_led(RED_LED, 1)
            flash_led(RED_LED, 1)

    finally:
        GPIO.cleanup()  # Clean up GPIO on exit

if __name__ == "__main__":
    quiz()
