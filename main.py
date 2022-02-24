import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

option = st.sidebar.selectbox("Topic", ("Main", "Toolbox", "About me"))

if option == "Main":
    st.title("Physics with a snake :snake:")
    st.markdown("Welcome to my very first web-app. It's gonna consist on Phisycs' stuff related with Python.")
    st.latex(r"\textbf{F}=\dfrac{d\textbf{p}}{dt}")
elif option == "Toolbox":
    reg_available = False
    st.markdown("Write below your comma-separated x values")
    x_list = st.text_area("x").split(",")
    st.markdown("Write below your comma-separated y values")
    y_list = st.text_area("y").split(",")
    try:
        X = np.array([])
        Y = np.array([])
        for i in range(len(x_list)):
            X = np.append(X, float(x_list[i]))
            Y = np.append(Y, float(y_list[i]))

        try:
            st.markdown("Check your input:")
            df = pd.DataFrame(data=(X, Y), columns=["x", "y"], index=None)
            st.table(df)
            model = linear_model.LinearRegression()
            model.fit(X.reshape(-1,1), Y, sample_weight=None)
            m = round(float(model.coef_),3)
            n = round(float(model.intercept_),3)
            X_r = np.array([0, max(X)])
            Y_r = np.array([m * 0 + n, m * max(X) + n])
            fig, ax = plt.subplots()
            ax.plot(X_r, Y_r, color="red")
            ax.scatter(X, Y)
            st.pyplot(fig)
            st.latex(f"y={m}x+{n}")

        except ValueError:
            st.write("Value error")

    except ValueError:
        st.write("Assure that x and y are CSV and both have the same amount of values!")
