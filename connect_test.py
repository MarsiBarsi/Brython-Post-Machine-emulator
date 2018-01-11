from browser import document, alert

# bind event 'click' on button to function echo
@document["mybutton"].bind("click")
def echo(ev):
    alert(document["zone"].value)
    document.write("hello1")
    document <= "Hello2"

document.write("hello5\n")
document <= "Hello6"
