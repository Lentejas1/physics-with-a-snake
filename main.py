import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import r2_score

option = st.sidebar.selectbox("Topic", ("Main", "Toolbox", "About me"))


def py_download(x, y, xlab="$x$", ylab="$y$"):
    xarray = "np.array(["
    yarray = "np.array(["
    labx = f"'{xlab}'"
    laby = f"'{ylab}'"

    for j in range(len(x)):
        if j != len(x) - 1:
            xarray += f"{x[j]},"
            yarray += f"{y[j]},"
        else:
            xarray += f"{x[j]}"
            yarray += f"{y[j]}"

    xarray += "])"
    yarray += "])"

    return str("import numpy as np" + "\n" + "import pandas as pd" + "\n" + "import matplotlib.pyplot as plt" "\n" +
                   "from sklearn import linear_model" + "\n" + "from sklearn.metrics import r2_score" + "\n" + f"X = {xarray}" + "\n" +
                   f"Y = {yarray}" + "\n" +
                   "model = linear_model.LinearRegression()" + "\n" +
                   "model.fit(X.reshape(-1, 1), Y, sample_weight=None)" + "\n" +
                   "m = round(float(model.coef_), 3)" + "\n" +
                   "n = round(float(model.intercept_), 3)" + "\n" +
                   "X_r = np.array([min(X), max(X)])" + "\n" +
                   "Y_r = np.array([m * min(X) + n, m * max(X) + n])" + "\n" +
                   "fig, ax = plt.subplots()" + "\n" +
                   "plt.grid()" + "\n" +
                   "ax.plot(X_r, Y_r, color='red')" + "\n" +
                   "ax.scatter(X, Y)" + "\n" +
                   f"plt.xlabel(" + f"{labx}" + ")\n" +
                                                f"plt.ylabel(" + f"{laby}" + ")\n" +
                                                                             "plt.show()")


if option == "Main":
    st.title("Physics with a snake :snake:")
    st.markdown("Welcome to my very first web-app. It's gonna consist on Phisycs' stuff related with Python.")
    st.latex(r"\textbf{F}=\dfrac{d\textbf{p}}{dt}")
    st.markdown("We have a **linear regression calculator** in the *Toolbox* page which can be used to calculate your "
                "own linear models and plot them.")
    st.markdown("Page created with :heart: by [Carlos Herrera](https://www.linkedin.com/in/carlos-herrera-vázquez-6218911b3).")
elif option == "Toolbox":
    st.title("Linear regression calculator")
    reg_available = False
    st.markdown("Write below your comma-separated x values")
    x_list = st.text_input("x").split(",")
    xlabel = st.text_input('x label')

    st.markdown("Write below your comma-separated y values")
    y_list = st.text_input("y").split(",")
    ylabel = st.text_input("y label")

    try:
        X = np.array([])
        Y = np.array([])
        for i in range(len(x_list)):
            X = np.append(X, float(x_list[i]))
            Y = np.append(Y, float(y_list[i]))

        try:
            check = st.checkbox('Check data')

            if check:
                st.markdown("Check your input:")
                df = pd.DataFrame(data=(X, Y), columns=["x", "y"], index=None)
                st.table(df)

            model = linear_model.LinearRegression()
            model.fit(X.reshape(-1, 1), Y, sample_weight=None)
            m = round(float(model.coef_), 3)
            n = round(float(model.intercept_), 3)
            X_r = np.array([min(X), max(X)])
            Y_r = np.array([m * min(X) + n, m * max(X) + n])
            st.markdown("Plotting temporarily not supported by Streamlit. You can download the code below so you can represent it on your own computer")
            Y_pred = np.array([])
            for i in range(len(X)): Y_pred = np.append(Y_pred, m * X[i] + n)
            r2 = round(r2_score(Y, Y_pred),3)
            st.latex(f"y={m}x+{n}")
            st.latex(f"r^2={r2}")
            st.download_button('Download .py', py_download(X, Y, xlabel, ylabel), file_name="plot.py")

        except ValueError:
            st.write("Value error")

    except ValueError:
        st.write("Assure that x and y are CSV and both have the same amount of values!")
