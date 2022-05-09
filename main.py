import turtle
import pandas


def update_title():
    screen.title(f"US State Game:score:{score}/50")


score = 0
screen = turtle.Screen()
update_title()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

tim = turtle.Turtle()
tim.hideturtle()
tim.penup()

data = pandas.read_csv("50_states.csv")
all_states=data["state"].to_list()
guessed_states=[]

def write_state_name(name):
    specific_state_list = data[data.state == answer_state]
    global score,guessed_states
    score += 1
    if len(specific_state_list) != 0:
        guessed_states.append(name)
        tim.goto(int(specific_state_list.x),int(specific_state_list.y))
        tim.write(f"{answer_state}", align="center")
        update_title()


is_game_on = True
missed_states=[]
while is_game_on:
    answer_state = screen.textinput(title="Guess The State", prompt="what's another state name:")
    answer_state=answer_state.title()  #converting title case
    if answer_state=="Exit":
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)
        print(len(missed_states))
        new_data=pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    write_state_name(answer_state)
turtle.mainloop()
