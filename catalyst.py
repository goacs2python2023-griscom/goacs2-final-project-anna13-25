from bokeh.plotting import figure, show
import numpy as np
import math
class jazz:
    f = figure()

    x = [-204.70, -192.12, -191.52, -191.41]
    y = [0.0788, 0.002, 0.0271, 0.489]
    f.circle(x, y, size = 8, color = "green")
    show(f)

class school:
     data = [46, 59, 71, 80]
     names = ["Performs Well on Standarized Tests", "Deep Understanding of Classroom Concepts", "Making Connections to Multiple Subjects", "Shows Problem Solving"]
     f2 = figure(x_range = names, height = 500, width = 1000, title = "Percentages of Students with High Creativity's Performace in School")
     f2.vbar(x = names, top = data, width = .6, color = "pink")

     f2.xgrid.grid_line_color = None
     f2.y_range.start = 0

     show (f2)

