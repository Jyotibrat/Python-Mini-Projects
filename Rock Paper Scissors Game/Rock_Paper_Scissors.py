import random

def get_cpu_move():
    return random.choice(['rock', 'paper', 'scissors'])

def get_player_move():
    options = ['rock', 'paper', 'scissors']
    player_input = input("Your choice? Rock, Paper, or Scissors: ").lower()
    
    if player_input not in options:
        print("\nInvalid choice! Try again.")
        return get_player_move()
    return player_input

def find_winner(player_move, cpu_move):
    if player_move == cpu_move:
        return "It's a tie! Great minds think alike."
    
    winning_moves = {
        'rock': 'scissors',   
        'scissors': 'paper',  
        'paper': 'rock'       
    }
    if winning_moves[player_move] == cpu_move:
        return "Congrats, you win!"
    else:
        return "The computer wins this time."

def start_game():
    print("\nWelcome to the game of Rock, Paper, Scissors!\n")
    
    cpu_move = get_cpu_move()
    player_move = get_player_move()
    
    print(f"\nYou chose: {player_move.capitalize()}")
    print(f"Computer chose: {cpu_move.capitalize()}")
    
    outcome = find_winner(player_move, cpu_move)
    print(f"\n{outcome}")

if __name__ == "__main__":
    start_game()