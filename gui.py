import Functions
import PySimpleGUI as sg

lable = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip="Enter a To-DO")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[[lable], [input_box, add_button]])
window.read()
window.close()
