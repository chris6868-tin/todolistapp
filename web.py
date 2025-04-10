import streamlit as st
import function

todos = function.load_data()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    function.save_data(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    check = st.checkbox(todo,key=todo)
    if check:
        todos.pop(index)
        function.save_data(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo,
              key="new_todo")
