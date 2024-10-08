import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_new = st.session_state["new_todo"] + '\n'
    functions.add_todo(todo_new)


st.title("My Todo App")
st.subheader("This an Todo app")
st.write("This app is to increase your productivity")


for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='',placeholder="Add a Todo ....",on_change=add_todo,key="new_todo")

