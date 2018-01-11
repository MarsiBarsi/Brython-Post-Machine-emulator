from browser import document, alert

# bind event 'click' on button to function echo
@document["mybutton"].bind("click")
def echo(ev):
    alert(document["zone"].value)
    document.write("hello1")
    document <= "Hello2"

variable = 25;
variable += 100;

array = []

for i in range 10:
    array.attend(i)

document <= variable,"\n"
document <= "=======\n"
document <= array
document <= "========"
document.write(array)
