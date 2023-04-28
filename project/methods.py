import numpy as np


def euler_integration(func, y0, t, beta, gamma, alpha, n):
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(1, len(t)):
        dt = t[i] - t[i - 1]
        if alpha is None:
            y[i] = y[i - 1] + func(y[i - 1], t[i - 1], beta, gamma, None, n) * dt
        else:
            y[i] = y[i - 1] + func(y[i - 1], t[i - 1], beta, gamma, alpha, n) * dt
    return y


def rk_integration(func, y0, t, beta, gamma, alpha, n):
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(1, len(t)):
        dt = t[i] - t[i - 1]
        k1 = func(y[i - 1], t[i - 1], beta, gamma, alpha, n)
        k2 = func(y[i - 1] + dt / 2 * k1, t[i - 1] + dt / 2, beta, gamma, alpha, n)
        k3 = func(y[i - 1] + dt / 2 * k2, t[i - 1] + dt / 2, beta, gamma, alpha, n)
        k4 = func(y[i - 1] + dt * k3, t[i - 1] + dt, beta, gamma, alpha, n)
        # if alpha is None:
        #     y[i] = y[i - 1] + dt * (k1 + k2 + k3) / 3
        # else:
        y[i] = y[i - 1] + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return y
