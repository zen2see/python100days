import pandas
import time
import random
from player import Player
from turtle import Turtle, Screen

# USING SELF
# class StateGame:
#     def __init__(self):
#         self.screen = self.setup_screen()
#         self.player = self.setup_player()
#         self.state_data = self.load_state_data()
#         self.all_states = self.get_state_list()
#         self.guessed_states = []
#         self.running = True
#         self.screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", self.close_game)

#     def setup_screen(self):
#         """Sets up the screen for the game."""
#         screen = Screen()
#         screen.title("U.S. States Game")
#         screen.bgcolor('black')
#         screen.colormode(255)
#         screen.setup(width=700, height=700)
#         screen.tracer(0)
#         image = "blank_states_img.gif"
#         screen.addshape(image)
#         screen.bgpic(image)
#         return screen

#     def setup_player(self):
#         """Sets up the player turtle."""
#         player = Turtle()
#         player.penup()
#         player.hideturtle()
#         return player

#     def flash_player(self):
#         """Flashes the player turtle to indicate a correct guess."""
#         self.player.color("yellow")
#         self.screen.update()
#         time.sleep(0.1)
#         self.player.color("blue")

#     def load_state_data(self):
#         """Loads state data from a CSV file."""
#         return pandas.read_csv("50_states.csv")

#     def get_state_list(self):
#         """Returns a list of all state names."""
#         return self.state_data.state.to_list()

#     def display_state(self, state_name):
#         """Displays the state name at the correct coordinates on the map."""
#         state_info = self.state_data[self.state_data.state == state_name]
#         if not state_info.empty:
#             x, y = int(state_info.x.iloc[0]), int(state_info.y.iloc[0])
#             self.player.goto(x, y)
#             self.player.write(state_name, align="center", font=("Courier", 12, "normal"))

#     def get_mouse_click_coordinates(self, x, y):
#         """Prints the coordinates where the mouse is clicked."""
#         print(f"Mouse clicked at ({x}, {y})")

#     def prompt_user_for_state(self):
#         """Prompts the user to guess a state name."""
#         answer_state = self.screen.textinput(title=f"{len(self.guessed_states)}/50 States Correct", prompt="What's another state's name?")
#         if answer_state:
#             return answer_state.title()
#         return None

#     def validate_guess(self, answer_state):
#         """Validates the user's guess and updates the guessed states list."""
#         if answer_state in self.all_states:
#             self.guessed_states.append(answer_state)

#     def get_unidentified_states(self):
#         """Returns a list of states that have not been guessed yet."""
#         return [state for state in self.all_states if state not in self.guessed_states]

#     def display_game_over(self):
#         """Displays the game over message."""
#         self.player.goto(0, 0)
#         self.player.write("GAME OVER", align="center", font=("Courier", 36, "bold"))

#     def close_game(self):
#         """Closes the game window."""
#         self.running = False
#         self.screen.bye()

#     def main(self):
#         while len(self.guessed_states) < 50 and self.running:
#             answer_state = self.prompt_user_for_state()
#             if answer_state:
#                 if answer_state.lower() == "exit":
#                     self.close_game()
#                     break
#                 self.validate_guess(answer_state)
#                 self.display_state(answer_state)
        
#         if self.running:  # Check if the screen is still active before setting up the click event
#             self.screen.onscreenclick(self.get_mouse_click_coordinates)
#             self.screen.mainloop()  # Keep screen open
#             self.screen.exitonclick()  # Exit on click

#         # Print the states not guessed after the loop ends
#         missing_states = self.get_unidentified_states()
#         if missing_states:
#             print(missing_states)
#             missing_states_list = pandas.DataFrame(missing_states)
#             missing_states_list.to_csv("Missing_States.csv")

# if __name__ == '__main__':
#     game = StateGame()
#     game.main()


# WITHOUT SELF 
"""Sets up the screen for the game."""
def setup_screen():
    screen = Screen()
    screen.title("U.S. States Game")
    screen.bgcolor('black')
    screen.colormode(255)
    screen.setup(width=700, height=700)
    screen.tracer(0)
    image = "blank_states_img.gif"
    screen.addshape(image)
    screen.bgpic(image)
    return screen

"""Flashes the player turtle to indicate a correct guess."""
def flash_player(player):
    player.color("yellow")
    screen.update()
    time.sleep(0.1)
    player.color("blue")

"""Loads state data from a CSV file."""
def get_statedata():
    statedata = pandas.read_csv("50_states.csv")
    return statedata

"""Returns a list of all state names."""
def get_data_into_list(statedata):
    all_states = get_statedata().state.to_list()
    return all_states

"""Displays the state name at the correct coordinates on the map."""    
def display_state(player, state_name, statedata):
    state_data = statedata[statedata.state == state_name]
    if not state_data.empty:
        # x, y = int(state_data.x), int(state_data.y)
        """ 
        INDEX LOCATION
        .iloc[0]:  This uses integer-based indexing to select the first element (index 0)
        from the specified column. 
        """
        x, y = int(state_data.x.iloc[0]), int(state_data.y.iloc[0])
        player.goto(x, y)
        player.write(state_name, align="center", font=("Courier", 12, "normal"))

"""Prints the coordinates where the mouse is clicked."""
def get_mouse_click_coor(x, y):
    print(f"Mouse clicked at ({x}, {y}")

"""Prompts the user to guess a state name."""
def ask_question(guessed_states, screen):
    # screen = Screen()
    #answer_state = screen.textinput(title=f"Guess the State", prompt="What's another state's name?")
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's the state's name?")
    # Check to make sure there is text in the answer before converting the case with title()
    if answer_state:
        return answer_state.title()
    return None

"""Validates the user's guess and updates the guessed states list."""
def check_answer(answer_state, guessed_states, all_states):
    if answer_state in all_states:
        guessed_states.append(answer_state)

"""Returns a list of states that have not been guessed yet."""
def get_states_not_guessed(guessed_states, all_states):
    missing_states = [state for state in all_states if state not in guessed_states]
    # print(missing_states)
    return missing_states

"""Displays the game over message."""
def game_over(player):
    player.goto(0, 0)
    player.write("GAME OVER", align="center", font=("Courier", 36, "bold"))

"""Closes the game window."""
def close_program(screen, running):
    running[0] = False
    screen.bye()

def main():
    screen = setup_screen()
    player = Turtle()
    player.penup()
    player.hideturtle()
    statedata = get_statedata()
    all_states = get_data_into_list(statedata)
    guessed_states = []
    running = [True]  # Use a list to allow modification within close_program

    screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", lambda: close_program(screen, running))
    while len(guessed_states) < 5 and running[0]:
        answer_state = ask_question(guessed_states, screen)
        if answer_state:
            if answer_state.lower() == "exit":
                close_program(screen, running)
                break
            check_answer(answer_state, guessed_states, all_states)
            display_state(player, answer_state, statedata)
            #get_states_not_guessed(guessed_states, all_states)
    if running[0]:  # Check if the screen is still active before setting up the click event
        screen.onscreenclick(get_mouse_click_coor)
        screen.mainloop() # Keep screen open
        screen.exitonclick() # Exit on click  
  
    # Print the states not guessed after the loop ends
    missing_states = get_states_not_guessed(guessed_states, all_states)
    if missing_states:
        # print(missing_states)
        missing_states_list = pandas.DataFrame(missing_states)
        missing_states_list.to_csv("Missing_States.csv")
    
if __name__ == '__main__':
    main()
   
"""
Convert the guess to Title case
Check if the guess ig among the 50 states
Write correc tguesses onto the map
Use a loop to allow the user to keep guessing
Recod the correct guees in a list
Keep Track of the score
"""

