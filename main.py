import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50.", prompt="What's another state's name?").title()

    if user_answer in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(user_answer)
        guessed_states.append(user_answer)
    elif user_answer == "Exit":
        for state in all_states:
            print(state)
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

screen.exitonclick()
