from random import randint


def guess_a_number():
    """Game to guess a number the computer randomly generated."""
    x = check_raw()
    random_number=randint(0,100)
    count_tries = 0

    while x != random_number:
        count_tries = count_tries + 1
        if count_tries == 10:
            print ('GAME OVER! You failed too many times!')
            break
        x = evaluate_my_number(x,random_number)
        if x == random_number:
            print ('Your number is correct! You needed {} tries.'.format(count_tries))
            break

    new_game = str(input("Do you want to play again? If so, say 'yes'! If not, say 'no' "))
    if new_game == 'yes':
        guess_a_number()
    else:
        print('Goodbye!')

    # TODO:
    # generate a random number (uniformly distributed between 0 and 100)
    # read input from the user and validate that the input is numeric (use the function check_raw)
    # check whether the number was guessed 
    # implement the functions evaluate_my_number, which checks whether the number is too high or too low
    # and print this information to the user
    # let the computer guess, therefore implement the demo_a_number function
    


def check_raw(print_string='Please try again: '):
    """Gets the string, raw_input should print, checks and returns the input."""
    try:
        x = int(input("Please guess a number between 0 and 100! You have 10 guesses"))
    except:
        print('Please try again!')
        x = check_raw()
    return x



def evaluate_my_number(guess, random_number):
    """Is the guess to high or to low? Guess again!"""
    if guess < random_number:
        print('Too low!')
    else: 
        print ('Too high!')
    guess = check_raw()
    return guess


def demo_a_number(random_number):
    """The computer tries to guess the number"""
    
guess_a_number()
