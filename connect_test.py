# First of all, the import of some libraries
from browser import document as doc
from browser import html

document <= "Hello world !"



# All the elements will be inserted in the div with the "container" id
container = doc['container']

# We create a new div element
newdiv = html.DIV(id = "new-div")
# Now we add some style
newdiv.style = {"padding": "5px",
               "backgroundColor": "#ADD8E6"}

# Now, lets add a table with a column with numbers and a
# column with a word on each cell
text = "Brython is really cool"
textlist = text.split()
table = html.TABLE()
for i, word in enumerate(textlist):
    table <= html.TR(html.TD(i + 1) +
                     html.TD(word))
# Now we add some style to the table
table.style = {"padding": "5px",
               "backgroundColor": "#aaaaaa",
               "width": "100%"}
# Now we add the table to the new div previously created
newdiv <= table + html.BR()

# a form? why not?
form = html.FORM()
input1 = html.INPUT(type="text", name="firstname", value="First name")
input2 = html.INPUT(type="text", name="lastname", value="Last name")
input3 = html.BUTTON("Button with no action!")
form <= input1 + html.BR() + input2 + html.BR() + input3

newdiv <= form + html.BR()

# Finally, we will add something more 'HTML5istic', a canvas with
# a color gradient in the newdiv previously created and below the form
canvas = html.CANVAS(width = 300, height = 300)
canvas.style = {"width": "100%"}
ctx = canvas.getContext('2d')
ctx.rect(0, 0, 300, 300)
grd = ctx.createRadialGradient(150, 150, 10, 150, 150, 150)
grd.addColorStop(0, '#8ED6FF')
grd.addColorStop(1, '#004CB3')
ctx.fillStyle = grd
ctx.fill()

newdiv <= canvas

# And finally we append the newdiv element
# to the parent, in this case the div with the "container" id
container <= newdiv
