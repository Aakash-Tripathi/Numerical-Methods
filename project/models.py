import numpy as np


def sir_model(sir, t, beta, gamma, alpha, n):
    s, i, r = sir
    ds_dt = -beta * s * i / n
    di_dt = beta * s * i / n - gamma * i
    dr_dt = gamma * i
    return np.array([ds_dt, di_dt, dr_dt])


def seir_model(seir, t, beta, gamma, alpha, n):
    s, e, i, r = seir
    ds_dt = -beta * s * i / n
    de_dt = beta * s * i / n - alpha * e
    di_dt = alpha * e - gamma * i
    dr_dt = gamma * i
    return np.array([ds_dt, de_dt, di_dt, dr_dt])
