import magpylib as magpy
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


def run():
    st.title(r"$\vec{B}$ produced by a solenoid :satellite:")

    coil = magpy.Collection()

    current = st.slider("Current (A):", min_value=0, max_value=20, step=1)
    loops = st.slider("Loops:", min_value=1, max_value=100, step=1)
    diametre = st.slider("Diameter (mm):", min_value=0.1, max_value=10.0, step=0.1)
    distance = st.slider("Distance between loops (mm):", min_value=0.01, max_value=1.00, step=0.01)

    for i in range(loops):
        espira = magpy.current.Circular(current=current, diameter=diametre, position=(0, 0, i*distance))
        coil.add(espira)

    fig = plt.figure(figsize=(10,4))
    ax1 = fig.add_subplot(121, projection='3d')
    fig1 = coil.display(markers=[(0,0,0)], axis=ax1)

    ax2 = fig.add_subplot(122,)
    ts = np.linspace(-distance*loops*1.5, distance*loops*1.5, 30)
    grid = np.array([[(x,0,z) for x in ts] for z in ts])
    B = magpy.getB(coil, grid)
    amp = np.linalg.norm(B, axis=2)
    strm = ax2.streamplot(grid[:,:,0], grid[:,:,2], B[:,:,0], B[:,:,2],density=2, color=np.log(amp), linewidth=1, cmap='autumn')
    cb = fig.colorbar(strm.lines)
    cb.set_label(r"|$\vec{B}$| [mT]")

    ax2.set_xlabel("$x$ [mm]")
    ax2.set_ylabel("$z$ [mm]")

    st.pyplot(fig)