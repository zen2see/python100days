import pandas
import time
import random
from player import Player
from turtle import Turtle, Screen

class StateGame:
    def __init__(self):
        self.screen = self.setup_screen()
        self.player = Player()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 36, "bold"))

    def setup_screen(self):
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

    def flash_player(self):
        self.player.color("yellow")
        self.screen.update()
        time.sleep(0.1)
        self.player.color("blue")

    def main(self):
        self.screen.mainloop()
    

if __name__ == '__main__':
    game = StateGame()
    game.main()
    


