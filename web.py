import streamlit as st
import functions
import os


def add_todo():
    task = st.session_state["new_todo"]
    todos.append(task + "\n")
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my minimalist todo app.")
st.write("This app is to increase your productivity.")

for todo in todos:
    checked = st.checkbox(todo, key=todo)
    if checked:
        todos.remove(todo)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter todo", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
