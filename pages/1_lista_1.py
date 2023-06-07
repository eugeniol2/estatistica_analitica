import streamlit as st

st.title("Lista 1")

import streamlit as st

navigation = [ "Questão 1", "Questão 2"]
selection = st.sidebar.radio("Questões", navigation)

    
if selection == "Questão 1":
    st.header("Descrição da questão 1")
    nested_navigation_1 = ["A", "B"]
    nested_selection_1 = st.sidebar.radio("Letras", nested_navigation_1)
    
    if nested_selection_1 == "A":
        st.subheader("Descrição da letra A")
        code = '''def hello():
        print("Hello, Streamlit!")'''
        st.code(code, language='python')
        
    elif nested_selection_1 == "B":
        st.subheader("Descrição da letra B")
        
elif selection == "Questão 2":
    st.header("Descrição da questão 2")
    # Add content for the second nested page
    
    # Add a nested sub-navigation
    nested_navigation_2 = ["Subpage 1", "Subpage 2"]
    nested_selection_2 = st.sidebar.radio("Nested Navigation", nested_navigation_2)
    
    if nested_selection_2 == "Subpage 1":
        st.subheader("Subpage 1")