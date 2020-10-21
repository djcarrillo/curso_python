from bokeh.plotting import figure, output_file, show
import numpy as np

if __name__ == "__main__":
    output_file('New Graph.html')
    fig = figure()
    x_vals = np.arange(0, 10, 0.1)
    y_vals = 2*np.sin(2*x_vals)
    fig.line(x_vals, y_vals, line_width=2)
    show(fig)


