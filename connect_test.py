from browser import document, alert



@document['do_one'].bind('click')
def do_one(event):
    if band[position[0]] == 0:
        band[position[0]] = 1
        refresh()


@document['do_null'].bind('click')
def do_null(event):
    if band[position[0]] == 1:
        band[position[0]] = 0
        refresh()

@document['right'].bind('click')
def right(event):
    position[0] += 1
    document["main_cat"].style.transform = "translate({}px,0)".format((position[0]-7-start_position)*46)
    refresh()

@document['left'].bind('click')
def left(event):
    position[0] -= 1
    document["main_cat"].style.transform = "translate({}px,0)".format((position[0]-7-start_position)*46)
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

start_position = 50

band = [0 for i in range (100)]

position = [(start_position+7)]

out_string = array_string()

document["zone15"].textContent = out_string
