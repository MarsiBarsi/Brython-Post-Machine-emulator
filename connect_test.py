from browser import document, alert


@document['do_one'].bind('click')
def do_one(event):
    if array[position[0]] == 0:
        array[position[0]] = 1
        refresh()


@document['do_null'].bind('click')
def do_null(event):
    if array[position[0]] == 1:
        array[position[0]] = 0
        refresh()

@document['right'].bind('click')
def right(event):
    position[0] += 1
    refresh()

@document['left'].bind('click')
def left(event):
    position[0] -= 1
    refresh()

@document['end_of_program'].bind('click')
def end_of_program(event):
    document["zone15"].textContent = 'done'

def refresh():
    out_string = array_string()
    document["zone15"].textContent = out_string

def array_string():
    out_string = ' | '
    for i in range (15):
        out_string += str(array[i])
        out_string += ' | '
    return out_string

array = [0 for i in range (100)]

position = [7]

out_string = array_string()

document["zone15"].textContent = out_string
