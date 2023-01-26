import streamlit as st

from func import read, write

todo = read()


def add_todo():
    """This function is to add item from  text input"""
    todo_ = st.session_state['item']+'\n'
    todo.append(todo_)
    write(todo)


st.title('My First To Do App')
st.header('This is Header ')
st.subheader('This is sub-header')
st.text('This is a simple text')
st.write ('This will improve your productivity')
st.warning('Warning!!!')

for index, item in enumerate(todo):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todo.pop(index)
        write(todo)
        del st.session_state[item]
        st.experimental_rerun()

st.text_input(label='Insert new item', placeholder='Add new item....', on_change=add_todo, key='item')

