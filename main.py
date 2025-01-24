import turtle
import pandas

data=pandas.read_csv("50_states.csv")
all_state=data.state.to_list()

screen=turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

#this code is used to get coordinate for where the mouse is been clicked
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

guessed_state=[]

while len(guessed_state)<50:
    answer_states=(screen.textinput(title=f"{len(guessed_state)}/50 States correct", prompt="What's another state's name?")).title()#render on the screen
    if answer_states=="Exit":
        missing_state=[]
        for state in all_state:
            if state not in guessed_state:
                missing_state.append(state)
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_states in all_state:
        guessed_state.append(answer_states)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_states]
        t.goto(state_data.x.item(),state_data.y.item())#.item is very important to not to get error
        t.write(answer_states)