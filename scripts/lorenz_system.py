import numpy as np
from scipy.integrate import solve_ivp

def lorenz(t, state, sigma, rho, beta):
    x, y, z = state
    return(sigma * (y - x), x * (rho - z) - y, x * y - beta * z)

def solve_lorenz(
    sigma=10.0, rho=28.0, beta=8/3,
    state0=None, t_span=(0.0, 50.0),
    n_points=10_000, method='RK45',
    rtol=1e-6, atol=1e-9, dense_output=False
):
    if state0 is None:
        state0=[1.0, 1.0, 1.0]
    if dense_output:
        sol = solve_ivp(
            lorenz, t_span, state0,
            args=(sigma, rho, beta),
            method=method, rtol=rtol, atol=atol, dense_output=True,
        )
        t = np.linspace(t_span[0], t_span[1], n_points)
        y = sol.sol(t)
        return t, y
    else:
        t_eval = np.linspace(t_span[0], t_span[1], n_points)
        sol = solve_ivp(
            lorenz, t_span, state0, t_eval=t_eval,
            args=(sigma, rho, beta),
            method=method, rtol=rtol, atol=atol
        )
        return sol.t, sol.y