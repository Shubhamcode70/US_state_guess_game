import pandas
from turtle import Turtle, Screen
from score import  Score

screen = Screen()
score = Score()
screen.bgpic("blank_states_img.gif")

states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()
correct_ans = []

while True:
    user_input = screen.textinput(title = "Current Score", prompt="Enter State name").title()
    if user_input == "Q":
        rem_states = []
        for state in all_states:
            if state not in correct_ans:
                rem_states.append(state)

        rem_data = pandas.DataFrame(rem_states)
        rem_data.to_csv("rem_states.csv")
        exit()

    if user_input in all_states:
        correct_ans.append(user_input)
        row_at = states_data[states_data.state == user_input]
        point =  Turtle()
        point.hideturtle()
        point.penup()
        point.goto(int(row_at.x), int(row_at.y))
        point.write(f"{user_input}")
        score.update_score()
        # print(row_at)
        # print("present")

screen.exitonclick()