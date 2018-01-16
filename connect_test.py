from browser import document, alert

@document['button_band_left'].bind('click')
def button_band_left(event):
    start_position[0] -= 1
    main_cat_moving('right')
    refresh()

@document['button_band_right'].bind('click')
def button_band_right(event):
    start_position[0] += 1
    main_cat_moving('left')
    refresh()

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
    for i in range (start_position[0],start_position[0]+15):
        out_string += str(band[i])
        out_string += ' | '
    return out_string

def main_cat_moving(action):
    if action == 'right':
        main_cat_position[0] += 46
        document["main_cat"].style.transform = "translate({}px,{}px)".format(main_cat_position[0],main_cat_position[1])

    if action == 'left':
        main_cat_position[0] -= 46
        document["main_cat"].style.transform = "translate({}px,{}px)".format(main_cat_position[0],main_cat_position[1])

    if action == 'up':
        main_cat_position[1] -= 30
        document["main_cat"].style.transform = "animation: move 0.5s ease".format(main_cat_position[1])
        main_cat_position[1] += 30

start_position = [50]

main_cat_position = [0,-15,0]
document["main_cat"].style.transform = "translate({}px,{}px)".format(main_cat_position[0],main_cat_position[1])

band = [0 for i in range (100)]

position = [(start_position[0]+7)]

out_string = array_string()

document["zone15"].textContent = out_string
