from flask import Flask, request
import random

app = Flask(__name__)
randnum = random.randint(1, 20)  # Generate the random number globally
num_of_guesses = 0  # Track the number of guesses globally

@app.route("/")
def home():
    return '''
    <h1>Guess the Number Game</h1>
    <p>Guess a whole number between 1 and 20.</p>
    <p>Enter your guess below:</p>
    <form action="/game" method="GET">
        <input name="text" placeholder="Enter your guess">
        <input type="submit" value="Submit">
    </form>
    <p>Type "s" to reveal the answer, or "n" to start a new game.</p>
    '''

@app.route("/game")
def game():
    global randnum, num_of_guesses

    guess = request.args.get('text', '')

    if guess == "n":  # Start a new game
        randnum = random.randint(1, 20)
        num_of_guesses = 0
        return '''
        <p>New game started! Guess a number between 1 and 20.</p>
        <a href="/">Go back to the main page</a>
        '''

    if guess == "s":  # Reveal the answer
        return f'''
        <p>Cheater! The answer is {randnum}.</p>
        <a href="/">Go back to the main page</a>
        '''

    try:
        guess = int(guess)
    except ValueError:
        return '''
        <p>Invalid input. Please enter a whole number between 1 and 20.</p>
        <a href="/">Try again</a>
        '''

    num_of_guesses += 1

    if guess == randnum:
        result = f"Correct! You guessed the number in {num_of_guesses} guesses."
        randnum = random.randint(1, 20)  # Start a new game automatically
        num_of_guesses = 0
        return f'''
        <p>{result}</p>
        <p>A new number has been generated. Try guessing again!</p>
        <a href="/">Go back to the main page</a>
        '''
    elif guess < randnum:
        return '''
        <p>Your guess is too low. Try again!</p>
        <a href="/">Go back to the main page</a>
        '''
    else:
        return '''
        <p>Your guess is too high. Try again!</p>
        <a href="/">Go back to the main page</a>
        '''

if __name__ == "__main__":
    app.run(debug=True)
