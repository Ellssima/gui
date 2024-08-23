import function
import FreeSimpleGUI as sg


label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter to-do', key='todo')
add_button = sg.Button('Add')

window = sg.Window('My to-do app',
                                    layout=[[label], [input_box, add_button]],
                                    font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = function.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            function.write_todos(todos)
        case WIN_CLOSED:
            break

window.close()