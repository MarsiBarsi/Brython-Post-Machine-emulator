from browser import document, alert
import time


@document['do_one'].bind('click')
def do_one(event):
    if band[position[0]] == 0:
        band[position[0]] = 1
        main_cat_moving('up')
        refresh()


@document['do_null'].bind('click')
def do_null(event):
    if band[position[0]] == 1:
        band[position[0]] = 0
        main_cat_moving('up')
        refresh()

@document['right'].bind('click')
def right(event):
    position[0] += 1
    main_cat_moving('right')
    refresh()

@document['left'].bind('click')
def left(event):
    position[0] -= 1
    main_cat_moving('left')
    refresh()

@document['end_of_program'].bind('click')
def end_of_program(event):
    document["band"].textContent = 'done'

def refresh():
    out_string = array_string()
    document["band"].textContent = out_string

def array_string():
    out_string = ' | '
    for i in range (start_position,start_position+15):
        out_string += str(band[i])
        out_string += ' | '
    return out_string

def main_cat_moving(action):
    if action == 'right':
        main_cat_position[0] += 46
        document["main_cat"].style.transform = "translate({}px,0)".format(main_cat_position[0])

    if action == 'left':
        main_cat_position[0] -= 46
        document["main_cat"].style.transform = "translate({}px,0)".format(main_cat_position[0])

    if action == 'up':
        main_cat_position[1] -= 30
        document["main_cat"].clear
        document["main_cat"] <= html.IMG(src='/images/3.png', width=87, height=87)
        document["main_cat"].style.transform = "translate({}px,{}px)".format(main_cat_position[0],main_cat_position[1])
        main_cat_position[1] += 30
        time.sleep(0.2)
        document["main_cat"].style.transform = "translate({}px,{}px)".format(main_cat_position[0],main_cat_position[1])
        document["main_cat"].clear
        document["main_cat"] <= html.IMG(src='/images/2.jpg', width=45, height=122)

start_position = 50

main_cat_position = [0,0,0]

band = [0 for i in range (100)]

position = [(start_position+7)]

out_string = array_string()

document["zone15"].textContent = out_string
