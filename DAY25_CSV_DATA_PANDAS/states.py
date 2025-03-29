import pandas
import time
import random
from player import Player
from turtle import Turtle, Screen

# class StateGame:
#     def __init__(self):
#         self.screen = self.setup_screen()
#         self.player = Player()

#     def game_over(self):
#         self.goto(0, 0)
#         self.write("GAME OVER", align="center", font=("Courier", 36, "bold"))

#     def setup_screen(self):
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

#     def flash_player(self):
#         self.player.color("yellow")
#         self.screen.update()
#         time.sleep(0.1)
#         self.player.color("blue")

#     def get_mouse_click_coord(x,y)
#         print(x,y)

#     def main(self):
#         self.screen.mainloop()

#  if __name__ == '__main__':
#     game = StateGame()
#     game.main()

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

def flash_player(player):
    player.color("yellow")
    screen.update()
    time.sleep(0.1)
    player.color("blue")

def get_statedata():
    statedata = pandas.read_csv("50_states.csv")
    return statedata

def get_data_into_list():
    all_states = get_statedata().state.to_list()
    return all_states
    
def display_state(player, state_name):
    state_data = get_statedata[get_statedata.state == state_name]
    if not state_data.empty:
        # x, y = int(state_data.x), int(state_data.y)
        x, y = int(state_data.x.iloc[0]), int(state_data.y.iloc[0])
        player.goto(x, y)
        player.write(state_name, align="center", font=("Courier", 12, "normal"))

def get_mouse_click_coor(x, y):
    print(f"Mouse clicked at ({x}, {y}")

def ask_question():
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    return answer_state.title()

def check_answer():
    if ask_question() in get_data_into_list().title():
        state
        question_result == ask_question()  
    
def game_over(player):
    player.goto(0, 0)
    player.write("GAME OVER", align="center", font=("Courier", 36, "bold"))

def main():
    global screen
    screen = setup_screen()
    player = Turtle()
    player.penup()
    player.hideturtle()
    statedata = get_data_into_list()
    display_state(player, ask_question(), )
    print(check_answer())
    #print(get_data_into_list())
    # display_state(player, "California", states_data)
    # display_state(player, "Texas", states_data)
    # display_state(player, "New York", states_data)
    screen.onscreenclick(get_mouse_click_coor)
    screen.mainloop()
    
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

