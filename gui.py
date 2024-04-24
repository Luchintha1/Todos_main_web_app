import Functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass


sg.theme("DarkGrey16")

clock = sg.Text('', key='clock')

lable = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip="Enter a To-DO", key='todo')
add_button = sg.Button("Add")

list_box = sg.Listbox(values=Functions.get_todos(), key='todos',
                      enable_events=True, size=(45,10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
#exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[clock],[lable],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           #[exit_button]
                           ],
                   font=('Calibre', 14))

while True:
    try:
        # event is the thing we pressed
        # value is the thing we add
        # Windows.read() will return a tuple.
        event, values = window.read() #(timeout=500)
        #window["clock"].update(value=time.strftime("%d - %b - %y   %H:%M:%S"))

        match event:
            case 'Add':
                todos = Functions.get_todos()
                new_todo = values['todo'] + '\n'
                todos.append(new_todo)
                Functions.set_todos(todos)
                window['todos'].update(values=todos)

            case 'Edit':
                try:
                    todo_to_edit = values['todos'][0]
                    new_todo = values['todo']

                    todos = Functions.get_todos()
                    index = todos.index(todo_to_edit)
                    todos[index] = new_todo + '\n'
                    Functions.set_todos(todos)
                    window['todos'].update(values=todos)
                except IndexError:
                    sg.popup("Please Select A Item", font=('Calibre', 14))

            case 'Complete':
                try:
                    todo_complete = values['todos'][0]
                    todos = Functions.get_todos()
                    todos.remove(todo_complete)
                    Functions.set_todos(todos)
                    window['todos'].update(values=todos)
                    window['todo'].update(value='')
                except IndexError:
                    sg.popup("Please Select A Item", font=('Calibre', 14))

            case 'Exit':
                break

            case 'todos':
                window['todo'].update(value=values['todos'][0].strip('\n'))

            case sg.WIN_CLOSED:
                break
    except:
        break


window.close()
