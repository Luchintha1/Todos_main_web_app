import streamlit as st
import Functions

todos = Functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    if len(todo) != 0:
        todos.append(todo)

    Functions.set_todos(todos)


st.title("Todo Web App")
st.write('Increase Productivity and Get Work Done.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        Functions.set_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Todo", label_visibility='hidden', placeholder='Add a new todo...',
              on_change=add_todo, key="new_todo")
