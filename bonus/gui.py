import function
import FreeSimpleGUI as sg


label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter to-do')
add_button = sg.Button('Add')

window = sg.Window('My to-do app', layout=[[label], [input_box, add_button]])
window.read()
print('hi')
window.close()