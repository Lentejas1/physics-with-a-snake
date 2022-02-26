import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import r2_score
import streamlit as st

def run():
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

        return str(
            f"import numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom sklearn import "
            f"linear_model\nfrom sklearn.metrics import r2_score\nX = {xarray}\nY = {yarray}\nmodel = "
            f"linear_model.LinearRegression()\nmodel.fit(X.reshape(-1, 1), Y, sample_weight=None)\nm = round(float("
            f"model.coef_), 3)\nn = round(float(model.intercept_), 3)\nX_r = np.array([min(X), max(X)])\nY_r = "
            f"np.array([m * min(X) + n, m * max(X) + n])\nfig, ax = plt.subplots()\nplt.grid()\nax.plot(X_r, Y_r, "
            f"color=\'red\')\nax.scatter(X, Y)\nplt.xlabel({labx})\nplt.ylabel({laby})\nplt.show()")

    st.title("Linear regression calculator :chart_with_upwards_trend:")
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
            fig, ax = plt.subplots()
            plt.grid()
            ax.plot(X_r, Y_r, color="red")
            ax.scatter(X, Y)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            st.pyplot(fig)
            Y_pred = np.array([])
            for i in range(len(X)): Y_pred = np.append(Y_pred, m * X[i] + n)
            r2 = round(r2_score(Y, Y_pred),3)
            
            if m == 1:
                if n > 0:
                    st.latex(f"y=x+{n}")
                elif n < 0:
                    st.latex(f"y=x{n}")
                else:
                    st.latex(f"y=x")
            else:
                if n > 0:
                    st.latex(f"y={m}x+{n}")
                elif n < 0:
                    st.latex(f"y={m}x{n}")
                else:
                    st.latex(f"y={m}x")

            st.download_button('Download .py', py_download(X, Y, xlabel, ylabel), file_name="plot.py")

        except ValueError:
            st.write("Value error")

    except ValueError:
        st.write("Assure that x and y are CSV and both have the same amount of values!")
