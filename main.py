import streamlit as st
import linearreg
import magsim

st.sidebar.title("**Physics with a snake** :snake:")
option = st.sidebar.selectbox("Topic", ("Main", "Toolbox", "About me"))


if option == "Main":
    st.title("Physics with a snake :snake:")
    st.markdown("Welcome to my very first web-app. It's gonna consist on Phisycs' stuff related with Python.")
    st.latex(r"\textbf{F}=\dfrac{d\textbf{p}}{dt}")
    st.markdown("We have a **linear regression calculator** in the *Toolbox* page which can be used to calculate your "
                "own linear models and plot them.")
    st.markdown(
        "Page created with :heart: by [Carlos Herrera](https://www.linkedin.com/in/carlos-herrera-vázquez-6218911b3).")
elif option == "Toolbox":
    ToolboxChoice = st.sidebar.radio("", ['Linear regression calc', r"$\vec{B}$ produced by a solenoid"])
    if ToolboxChoice == "Linear regression calc":
        linearreg.run()
    elif ToolboxChoice == r"$\vec{B}$ produced by a solenoid":
        magsim.run()
if option == "About me":
    st.title("About me :person:")
    st.markdown("Hey, there!\nMy name is Carlos and I'm a Physics' Undergraduate (2n grande currently). The aim of "
                "this web-site is to show what we can do with Python related with Physics at the same time I try to "
                "show you all how you can make it too.\nI hope you like it!")
