import streamlit as st
import Functions

todos = Functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    Functions.set_todos(todos)

st.title("To-Do Web App")
st.subheader('ToDos')
st.write('This app increase your productivity')

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder='Add a new todo...',
              on_change=add_todo, key="new_todo")

st.session_state