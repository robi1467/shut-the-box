import random
numbers_list = [1,2,3,4,5,6,7,8,9,10]
game_won = False
game_completed = False
#Stats
games_played = 0
games_won = 0
games_lost = 0
average_score = 0
total_score = 0

def welcome():
    welcome_message = "Welcome to shut the box"
    print(welcome_message)
    i = 0
    result = ""
    while i < len(numbers_list):
        if i < len(numbers_list)-1:
            result += str(numbers_list[i]) + " "
        else:
            result += str(numbers_list[i])
        i+=1
    print(result)

def dice_roll(amount):
    total = 0
    i = 0
    while i < amount:
        total += random.randint(1, 6)
        i+=1
    return total

def choose_dice_amount():
    amount = 0
    while True:
        try:
            amount = int(input("You choose to roll one or two dice. Please enter either '1' or '2': "))
        except ValueError:
            print("INVALID ENTRY PLEASE TRY AGAIN")
            continue
        if amount == 1 or amount == 2:
            return amount
        else:
            print("INVALID ENTRY PLEASE TRY AGAIN!")
            continue
    return amount

def choose_number_to_drop(target_amount):
    entered = 0
    goal = target_amount
    entered_numbers = list()
    while goal != 0:
        try:
            print("Available numbers: " + str(numbers_list) + " to get to " + str(target_amount))
            if len(entered_numbers) != 0:
                print("Numbers entered so far;" + str(entered_numbers))
            entered = int(input("Please enter a number that is available: "))
        except ValueError:
            print("Invalid Entry, please try again")
            continue
        if entered not in numbers_list or entered in entered_numbers:
            print("Invalid Entry, please try again")
            continue
        else:
            goal -= entered
            entered_numbers.append(entered)
            if goal < 0:
                goal = target_amount
                entered_numbers = list()
    i = 0
    while i < len(entered_numbers):
        numbers_list.remove(entered_numbers[i])
        i += 1

def check_lost_game(rolled):
    value = True
    if rolled not in numbers_list:
        i = 0
        while i < len(numbers_list):
            j = i+1
            while j< len(numbers_list):
                if numbers_list[i] + numbers_list[j] == rolled:
                    return False
                k = j+1
                while k < len(numbers_list):
                    if numbers_list[i] + numbers_list[j] + numbers_list[k] == rolled:
                        return False
                    l = k+1
                    while l < len(numbers_list):
                        if numbers_list[i] + numbers_list[j] + numbers_list[k] + numbers_list[l] == rolled:
                            return False
                        l+=1
                    k+=1
                j+=1
                
            i +=1
    else:
        value = False
    return value

def end_game():
    game_completed = True
    return game_completed

def win_game():
    game_won = True
    return game_won

def score_game():
    score = 0
    i = 0
    while i < len(numbers_list):
        score += numbers_list[i]
        i+=1
    return score

def all_less_than_7():
    less_than_7 = True
    i = 0
    while i < len(numbers_list):
        if numbers_list[i] > 6:
            less_than_7 = False
        i += 1
    return less_than_7
def keep_playing_input():
    while True:
        try:
            continue_playing = (input("Do you wish to keep playing? y or n: "))
        except ValueError:
            print("Invalid choice; please try again")
            continue
        if continue_playing.lower == "y":
            return True
        else:
            return False

keep_playing = True
while keep_playing:
    numbers_list = [1,2,3,4,5,6,7,8,9,10]
    welcome()
    roll_total = 0
    while roll_total < 55:
        dice_amount = 2
        if  all_less_than_7():
            dice_amount = choose_dice_amount()
        dice_total = dice_roll(dice_amount)
        print("Your roll is: " + str(dice_total))

        if check_lost_game(dice_total):
            print("It is impossible to continue the game with this roll")
            break

        choose_number_to_drop(dice_total)
        roll_total += dice_total

    if roll_total == 55:
       game_won = win_game()

    if game_won:
        print("Congrats you won!!!!")
        games_played +=1
        games_won +=1
    else:
        print("You lose, your score is " + str(score_game()))
        print("Numbers remaining: " + str(numbers_list))
        games_played += 1
        games_lost += 1
        total_score += score_game()
    average_score = total_score/games_played
    game_won = False
    print("STATS:\nGames Played: " + str(games_played) + "\nGames Won: " + str(games_won) + "\nGames Lost: " + str(games_lost)
    + "\nAverage Score: " + str(average_score) + "\nTotal Score: " + str(total_score))
    keep_playing_input()
    
