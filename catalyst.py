from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
import math
class jazz:
     f = figure(title = "Creativity Through Performace in Jazz Improvisation", width = 1000)

     x = [-204.70, -203.80, -192.12, -191.52, -191.41]
     y = [0.0788, 0.171, 0.002, 0.0271, 0.489]
     legend = ["Music Training", "Jazz Training", "With Experience", "With Instructions", "With Instructions and Experience"]

     f.circle(x[0], y[0], size = 10, color = "green", legend_label = legend[0])
     #music training
     f.circle(x[1], y[1], size = 10, color = "red", legend_label = legend[1])
     #jazz training
     f.circle(x[2], y[2], size = 10, color = "blue", legend_label = legend[2])
     #experience
     f.circle(x[3], y[3], size = 10, color = "purple", legend_label = legend[3])
     #instructions
     f.circle(x[4], y[4], size = 10, color = "turquoise", legend_label = legend[4])
     #instructions + experience
    
     f.legend.orientation = "horizontal"
     f.legend.location = "top_center"
    
     show(f)

class school:
     data = [46, 59, 71, 80]
     names = ["Performs Well on Standarized Tests", "Deep Understanding of Classroom Concepts", "Making Connections to Multiple Subjects", "Shows Problem Solving"]
     f2 = figure(x_range = names, height = 500, width = 1000, title = "Students with High Creativity Performace in School by Percent")
     f2.vbar(x = names, top = data, width = .6, color = "magenta")

     show (f2)

