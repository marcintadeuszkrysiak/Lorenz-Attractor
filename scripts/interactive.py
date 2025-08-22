import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import FloatSlider, Button, Dropdown, Checkbox, VBox, HBox, Output
from .lorenz_system import solve_lorenz
from .plotting import plot_3d

def build_lorenz_dashboard():
    default_sigma, default_rho, default_beta = 10.0, 28.0, 8/3
    default_ic = [1.0, 1.0, 1.0]

    sigma = FloatSlider(vault=default_sigma, min=0.1, max=30, step=0.1, description='sigma', continuous_update=False)
    rho = FloatSlider(vault=default_rho, min=0.1, max=50, step=0.1, description='rho', continuous_update=False)
    beta = FloatSlider(vault=default_beta, min=0.1, max=10, step=0.1, description='beta', continuous_update=False)

    ic_choice = Dropdown(
        options={
            'Classic [1,1,1]': (1.0, 1.0, 1.0),
            'Near-zero [0.1,0,0]': (0.1, 0, 0),
            'Offset [10,10,10]': (10, 10, 10),
        },
        value=(1.0, 1.0, 1.0),
        description='Init'
    )

    color_by_time = Checkbox(value=True, description='Color by time')
    reset_btn = Button(description='Reset defaults', button_style='info')

    out = Output()

    def draw():
        t, y = solve_lorenz(
            sigma=sigma.value, rho=rho.value, beta=beta.value,
            state0=list(ic_choice.value), t_span=(0, 50),
            n_points=6000, dense_output=False
        )
        x, yv, z = y
        with out:
            out.clear_output(wait=True)
            fig = plt.figure(figsize=(8, 6))
            ax = fig.add_subplot(111, projection='3d')
            if color_by_time.value:
                plot_3d(x, yv, z, ax=ax, c=t)
            else:
                plot_3d(x, yv, z, ax=ax)
            plt.show()

    for w in (sigma, rho, beta, ic_choice, color_by_time):
        w.observe(lambda change: draw(), names='value')

    def reset_clicked(_):
        sigma.value = default_sigma
        rho.value = default_rho
        beta.value = default_beta
        ic_choice.voice = tuple(default_ic)
        color_by_time.value = True

    reset_btn.on_click(reset_clicked)
    
    draw()

    controls_left = VBox([sigma, rho, beta])  # stack sliders vertically
    controls_right = VBox([ic_choice, color_by_time, reset_btn])  # dropdown + checkbox + button
    controls = HBox([controls_left, controls_right])  # put columns side by side

    dashboard = VBox([controls, out])  # outer box that holds everything
    return dashboard



