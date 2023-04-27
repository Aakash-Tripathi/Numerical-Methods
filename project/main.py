import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

from models import sir_model, seir_model
from methods import euler_integration, rk_integration


def update_plot(
    model_func, integration_func, t_start, t_end, dt, y0, beta, gamma, alpha, n
):
    t = np.arange(t_start, t_end, dt)
    y = integration_func(model_func, np.array(y0), t, beta, gamma, alpha, n)

    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(8, 4))

    if model_func == sir_model:
        labels = ["Susceptible", "Infected", "Recovered"]
    else:
        labels = ["Susceptible", "Exposed", "Infected", "Recovered"]
    # for i, label in enumerate(labels[: len(y0)]):
    ax.plot(t, y[:, i], label=labels)
    ax.set_xlabel("Time")
    ax.set_ylabel("Number of Individuals")
    ax.set_title("Model Simulation")
    ax.legend()
    ax.set_xlim(t_start, t_end)

    return fig


if __name__ == "__main__":
    st.set_page_config(page_title="Epidemiology Simulator", layout="wide")
    st.title("Epidemiology Simulator")

    model_options = ["SIR Model", "SEIR Model"]
    model_choice = st.sidebar.selectbox("Choose a Model", model_options)
    integration_options = ["Euler Method", "Runge-Kutta Method"]
    integration_choice = st.sidebar.selectbox(
        "Choose an Integration Method", integration_options
    )

    beta = st.sidebar.slider("Infection Rate", 0.0, 1.0, 0.2, step=0.01)
    gamma = st.sidebar.slider("Recovery Rate", 0.0, 1.0, 0.1, step=0.01)
    alpha = (
        st.sidebar.slider("Incubation Rate", 0.0, 1.0, 0.5, step=0.01)
        if model_choice == "SEIR Model"
        else None
    )
    n = st.sidebar.slider("Total Population", 1, 100000, 1000)
    t_start = st.sidebar.slider("Simulation Start Time", 0, 100, 0)
    t_end = st.sidebar.slider("Simulation End Time", 0, 1000, 100)
    dt = st.sidebar.slider("Time Step", 0.01, 1.0, 0.1, step=0.01)

    if model_choice == "SEIR Model":
        e0 = st.sidebar.number_input(
            "Initial Number of Exposed Individuals", value=1, step=1
        )
        i0 = st.sidebar.number_input(
            "Initial Number of Infected Individuals", value=0, step=1
        )
        r0 = st.sidebar.number_input(
            "Initial Number of Recovered Individuals", value=0, step=1
        )
        s0 = n - e0 - i0 - r0
        y0 = s0, e0, i0, r0
    else:
        i0 = st.sidebar.number_input(
            "Initial Number of Infected Individuals", value=1, step=1
        )
        r0 = st.sidebar.number_input(
            "Initial Number of Recovered Individuals", value=0, step=1
        )
        s0 = n - i0 - r0
        y0 = s0, i0, r0

    model_func = sir_model if model_choice == "SIR Model" else seir_model
    integration_func = (
        euler_integration if integration_choice == "Euler Method" else rk_integration
    )
    func_args = (
        (beta, gamma, alpha, n)
        if model_choice == "SEIR Model"
        else (beta, gamma, None, n)
    )
    fig = update_plot(model_func, integration_func, t_start, t_end, dt, y0, *func_args)

    st.pyplot(fig)
