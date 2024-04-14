import Functions
import PySimpleGUI as sg

lable = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip="Enter a To-DO", key='todo')
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[lable], [input_box, add_button]],
                   font=('Calibri', 14))

while True:
    # event is the thing we pressed
    # value is the thing we add
    # Windows.read() will return a tuple.
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case 'Add':
            todos = Functions.get_todos()
            new_todo = value['todo'] + '\n'
            todos.append(new_todo)
            Functions.set_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
