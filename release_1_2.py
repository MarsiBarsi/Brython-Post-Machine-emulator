from browser import document, alert, window, html

#----help:
@document['help'].bind('click')
def help_change(event):
    if status["help"] == 1:
        status["help"] = 0
        document["dummy-pois"].style.visibility = "hidden"
    else:
        status["help"] = 1
        document["dummy-pois"].style.visibility = "visible"

@document['tape_setting'].bind('click')
def tape_setting(event):
    status["help"] = 0
    document["dummy-pois"].style.visibility = "hidden"
    if status["tape_setting"] == 0:
        status["tape_setting"] = 1
        document["not_for_setting"].style.visibility = "hidden"
    else:
        status["tape_setting"] = 0
        document["not_for_setting"].style.visibility = "visible"


@document['rus_lang'].bind('click')
def lang_change_to_ru(event):
    document["text-1"].textContent = "Передвинуть ленту"
    document["text-2"].textContent = "Это бесконая лента машины Поста и кот-каретка. Каждая ячейка ленты может быть заполнена или пуста"
    document["text-3"].textContent = "Последовательность исполненных комманд"
    document["text-4"].textContent = "Следующая команда к исполнению"
    document["text-5"].textContent = "Если ячейка пуста, кот исполнит команду из первого поля. Если ячейка заполнена, то из второго."
    document["text-6"].textContent = "Завершить программу"
    document["help"].textContent = "Подзказки"
    document["tape_setting"].textContent = "Установка ленты"


@document['eng_lang'].bind('click')
def lang_change_to_eng(event):
    document["text-1"].textContent = "It moves the tape"
    document["text-2"].textContent = "It is an endless tape of Post Machine and cat-carriage who executes commands. Every cell can be filled or empty"
    document["text-3"].textContent = "Sequence of executed commands"
    document["text-4"].textContent = "The next command"
    document["text-5"].textContent = "If the cell is empty, cat executes command from the first field. If it is filled, cat executes command from the second field"
    document["text-6"].textContent = "End the program"
    document["help"].textContent = "HELP"
    document["tape_setting"].textContent = "Set tape"


#----band moving:

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


#----commands:

@document['do_one'].bind('click')
def do_one(event):
    if status["tape_setting"] == 1:
        if band[position[0]] == 0:
            band[position[0]] = 1
            main_cat_moving('up')
            refresh()
        return

    commands.append([3,int(document["to_command"].value)])

    if status["tape_setting"] == 0:
        executable_command[1] += 1
        document["to_command"].value = executable_command[1]
        print_new_command()

    execute()



@document['do_null'].bind('click')
def do_null(event):
    if status["tape_setting"] == 1:
        if band[position[0]] == 1:
            band[position[0]] = 0
            main_cat_moving('up')
            refresh()
        return

    commands.append([4,int(document["to_command"].value)])
    if status["tape_setting"] == 0:
        executable_command[1] += 1
        document["to_command"].value = executable_command[1]
        print_new_command()

    execute()


@document['right'].bind('click')
def right(event):
    if status["tape_setting"] == 1:
        position[0] += 1
        main_cat_moving('right')
        refresh()
        return

    commands.append([2,int(document["to_command"].value)])
    executable_command[1] += 1
    document["to_command"].value = executable_command[1]
    print_new_command()

    execute()


@document['left'].bind('click')
def left(event):
    if status["tape_setting"] == 1:
        position[0] -= 1
        main_cat_moving('left')
        refresh()
        return

    commands.append([1,int(document["to_command"].value)])
    executable_command[1] += 1
    document["to_command"].value = executable_command[1]
    print_new_command()

    execute()

@document['one_or_null'].bind('click')
def one_or_null(event):
    commands.append([5,int(document["if_null"].value),int(document["if_one"].value)])

    executable_command[1] += 1
    document["to_command"].value = executable_command[1]

    print_new_command()
    execute()


@document['end_of_program'].bind('click')
def end_of_program(event):
    document["dummy-pois"].style.visibility = "hidden"
    document["commands_line"].style.visibility = "hidden"
    document["not_for_setting"].style.visibility = "hidden"
    commands.append([6,''])
    print_new_command()


#-----
#-----functions:
def execute():
    endless_catcher = 0
    while executable_command[0] < executable_command[1]:

        if commands[executable_command[0]][0] == 1:
            position[0] -= 1
            main_cat_moving('left')
            refresh()

        if commands[executable_command[0]][0] == 2:
            position[0] += 1
            main_cat_moving('right')
            refresh()

        if commands[executable_command[0]][0] == 3:
            if band[position[0]] == 0:
                band[position[0]] = 1
                main_cat_moving('up')
                refresh()

        if commands[executable_command[0]][0] == 4:
            if band[position[0]] == 1:
                band[position[0]] = 0
                main_cat_moving('up')
                refresh()

        if commands[executable_command[0]][0] == 5:
            if band[position[0]] == 0:
                executable_command[0] = commands[executable_command[0]][1]
                endless_catcher += 1
                continue;

            if band[position[0]] == 1:
                executable_command[0] = commands[executable_command[0]][2]
                endless_catcher += 1
                continue;


        executable_command[0] = commands[executable_command[0]][1]
        endless_catcher += 1
        if endless_catcher > 1000:
            document["band"].textContent = 'endless cycle :('
            break;

def print_new_command():
    new_command_string = str(executable_command[0])

    if commands[executable_command[0]][0] == 1:
        new_command_string += ' ← '

    if commands[executable_command[0]][0] == 2:
        new_command_string += ' → '

    if commands[executable_command[0]][0] == 3:
        new_command_string += ' V '

    if commands[executable_command[0]][0] == 4:
        new_command_string += ' ↕ '

    if commands[executable_command[0]][0] == 5:
        new_command_string += ' ? '
        new_command_string += str(commands[executable_command[0]][1])+','+str(commands[executable_command[0]][2])+' | '
        document["commands"].textContent += new_command_string
        return

    if commands[executable_command[0]][0] == 6:
        new_command_string += ' ! '

    new_command_string += str(commands[executable_command[0]][1])+' | '
    document["commands"].textContent += new_command_string


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
        document["main_cat"].style.visibility = "visible"
        document["main_cat"].style.transform = "translate({}px,{}px)".format(main_cat_position[0],main_cat_position[1])
    else:
        document["main_cat"].style.visibility = "hidden"

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
        main_cat_position[1] -= 30
        print_cat_moving()
        refresh()
        main_cat_position[1] += 30
        print_cat_moving()


#-----------initialization-----------
status = {"help" : 1, "tape_setting" : 0} # help is active, tape_setting - not
#---------Band:----------
band_size = 100

band = [0 for i in range (1,band_size)] #band of post machine
start_position = [band_size//2] #center of the band

#----cat:---------------
position = [(start_position[0]+7)] #coordinate of cat in center of band

main_cat_position = [0,-15,1] #x,y position of cat from center; third parametr is visibility

#-----commands:----------
# list of commands consists of comand-lists. every comand-list has three paramets
# 0 - command; 1 - number of next command
# codes of commands from post machine:
# ← : 1
# → : 2
# V : 3
# ↕ : 4
# ? : 5
# ! : 6
commands = [ [0,0] ] # format of commands list
executable_command = [1,2] # 0 - to execute at the moment; 1 - last command

#---------start:----------
out_string = array_string() #out_string is getting empty band

document["band"].textContent = out_string #print band

document["main_cat"].style.transform = "translate({}px,{}px)".format(main_cat_position[0],main_cat_position[1]) #cat is ready

document["commands"].textContent = " | "
