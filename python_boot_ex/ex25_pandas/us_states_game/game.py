import turtle
import pandas as pd

screen = turtle.Screen()
FONT = ("Arial", 10, "normal")
screen.title("U.S States Game")
image = "blank_states_img.gif"
states_csv = pd.read_csv("50_states.csv")
screen.tracer(0)
screen.addshape(image)
turtle.shape(image)

game_is_on = True
suc_num = 0
no_suc_arr = states_csv.state.to_list()

while suc_num <= 50:
    screen.update()
    # 첫문자를 대문자 나머지 소문자로 바꾸는 방법 -> title 메소드
    answer_state = screen.textinput(title=f"{suc_num}/50 States Correct",
                                    prompt="What's another state name?")

    if answer_state is None or answer_state == "Exit":
        break

    answer = states_csv[states_csv["state"] == answer_state.title()]

    if answer.empty:
        continue

    suc_num += 1

    write_turtle = turtle.Turtle()
    write_turtle.penup()
    write_turtle.hideturtle()

    # 판다스에서 해당 행,열의 밸류갑을 가져오는 방법 -> item 메소드
    write_turtle.goto(answer.x.item(), answer.y.item())
    write_turtle.write(f"{answer.state.item()}", align="center", font=FONT)
    no_suc_arr.remove(answer.state.item())

# states_to_learn.csv
learn_dict = {
    "states": no_suc_arr
}
learn_df = pd.DataFrame.from_dict(learn_dict)
learn_df.to_csv("states_to_learn.csv")
