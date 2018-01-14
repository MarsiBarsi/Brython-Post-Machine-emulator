from browser import document, alert

@document['button1'].bind('click')
def change_plus(event):
    array[position] += 1

@document['button2'].bind('click')
def change_pos(event):
    position += 1


@document['button3'].bind('click')
def change_minus(event):
    array[position] -= 1

@document["mybutton"].bind("click")
def echo(ev):
    out_string = array_string()
    document["zone15"].textContent = out_string

def array_string():
    out_string = '| '
    for i in range (15):
        out_string += str(array[i])
        out_string += ' | '
        out_string += str(position)
    return out_string

array = [0 for i in range (100)]

out_string = array_string()

position = 1


document["zone15"] <= out_string
