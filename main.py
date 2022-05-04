import turtle
import pandas as pd
screen = turtle.Screen()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

correct = 0
answer_track = []
missing_states = []

while len(answer_track) < 50:

  answer_state = screen.textinput(title='{}/50 States Correct'.format(correct), prompt='whats another state name?').lower()

  data = pd.read_csv('50_states.csv')

  if answer_state == 'exit':
    for x in data['state']:
      if x not in answer_track:
        missing_states.append(x)
    df = pd.DataFrame(missing_states)  
    df.to_csv('states_to_learn.csv', index=False)
    break

  data['state'] = data['state'].apply(lambda x : x.lower())
  for x in data['state']:
    if answer_state == x:
      answer_track.append(answer_state)
      t = turtle.Turtle()
      t.hideturtle()
      t.penup()
      pos = data[data['state'] == answer_state]
      t.goto((int(pos['x']),int(pos['y'])))
      t.write(answer_state)
      correct += 1 
      continue

# def get_mouse_click_coor(x,y):
#   print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


# screen.exitonclick()
