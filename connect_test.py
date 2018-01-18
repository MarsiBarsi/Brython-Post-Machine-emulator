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

def check_visibility():
    if -323 < main_cat_position[0] < 323: #in band
        return 1
    else:
        return 0

def print_cat_moving():
    if check_visibility() == 1:
        document["main_cat"].style.transform = "translate({}px,{}px)".format(main_cat_position[0],main_cat_position[1])
    else:
        document["main_cat"].style.transform = "translate({}px,{}px)".format(9999,9999) #invisible

def array_string():
    out_string = ' | '
    for i in range (start_position[0],start_position[0]+15):
        out_string += str(band[i])
        out_string += ' | '
    return out_string

def main_cat_moving(action):
    if action == 'right':
        main_cat_position[0] += 46
        print_cat_moving()

    if action == 'left':
        main_cat_position[0] -= 46
        print_cat_moving()

    if action == 'up':
        for i in range (1,30):
            main_cat_position[1] -= 1
            document["main_cat"].style.transform = "translate({}px,{}px)".format(main_cat_position[0],main_cat_position[1])
        refresh()
        for i in range (1,30):
            main_cat_position[1] += 1
            document["main_cat"].style.transform = "translate({}px,{}px)".format(main_cat_position[0],main_cat_position[1])


#-----------initialization-----------
#---------Band:----------
band_size = 100

band = [0 for i in range (1,band_size)] #band of post machine
start_position = [band_size//2] #center of the band

#----cat:---------------
position = [(start_position[0]+7)] #coordinate of cat in center of band

main_cat_position = [0,-15,1] #x,y position of cat from center; third parametr is visibility

#-----commands:----------
# list of commands consists of comand-lists. every comand-list has three paramets
# 0 - number of command; 1 - command; 2 - number of next command
# codes of commands from post machine:
# ← : 1
# → : 2
# V : 3
# ↕ : 4
# ? : 5
# ! : 6
commands = [ [0,0,0] ] # format of commands list

#---------start:----------
out_string = array_string() #out_string is getting empty band

document["band"].textContent = out_string #print band

document["main_cat"].style.transform = "translate({}px,{}px)".format(main_cat_position[0],main_cat_position[1]) #cat is ready
