from browser import document, alert

moving = document["rot15"]
x = 0
dx = 3
run = None

@document['button15'].bind('click')
def change(event):
    global run
    if run is None:
        # start animation
        animloop(1)
    else:
        # stop animation
        window.cancelAnimationFrame(run)
        run = None

def render():
    global x, dx
    moving.style.transform = "translate({}px,0)".format(x)
    x += dx
    if x > document["zone15"].offsetWidth-moving.offsetWidth:
        dx = -dx
        moving.html = "◄" # left triangle
    elif x <= 0:
        dx = -dx
        moving.html = "►" # right triangle

def animloop(t):
    global run
    run = window.requestAnimationFrame(animloop)
    render()

# bind event 'click' on button to function echo
@document["mybutton"].bind("click")
def echo(ev):
    alert("rabotaet",document["zone"].value)
    document["zone15"] <= str(array,"\n",variable)

variable = 25;
variable += 100;

array = []

for i in range (10):
    array.append(i)
