import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import statistics
import random
#reading scores data
df = pd.read_csv("StudentsPerformance.csv")
data1 = df["reading score"].tolist()
data2 = df["math score"].tolist()
data3 = df["writing score"].tolist()
#Calculating the mean and the standard deviation
mean = sum(data) / len(data)
std_deviation = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)
#Finding 1 standard deviation stard and end values, and 2 standard deviations stard and end values
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
#Plotting the chart, and lines for mean, 1 standard deviation and 2 standard deviations
fig = ff.create_distplot([data1], ["reading score"], show_hist=False)
fig2 = ff.create_distplot([data2], ["math score"], show_hist=False)
fig3 = ff.create_distplot([data3], ["writing score"], show_hist=False)
# 
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
#
fig2.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig2.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig2.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig2.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig2.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
# 
fig3.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig3.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig3.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig3.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig3.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
# 
performance_math = df["math score"].to_list()
performance_reading = df["reading score"].to_list()
performance_writing = df["writing score"].to_list()
# 
performance_mean_math = statistics.mean(performance_math)
performance_mean_reading = statistics.mean(performance_reading)
performance_mean_writing = statistics.mean(performance_writing)
# 
performance_mean_math_std_deviation = statistics.stdev(performance_math)
performance_mean_reading_std_deviation = statistics.stdev(performance_reading)
performance_mean_writing_std_deviation = statistics.stdev(performance_writing)
# 
performance_median_math = statistics.median(performance_math)
performance_median_reading = statistics.median(performance_reading)
performance_median_writing = statistics.median(performance_writing)
# 
performance_mode_math = statistics.mode(performance_math)
performance_mode_reading = statistics.mode(performance_reading)
performance_mode_writing = statistics.mode(performance_writing)
# 
fig.show()
# 
print(" \n ¯\_( ͡° ͜ʖ ͡°)_/¯ MEAN FOR READING ¯\_( ͡° ͜ʖ ͡°)_/¯", performance_mean_reading)
print(" \n ¯\_( ͡° ͜ʖ ͡°)_/¯ MEDIAN FOR READING ¯\_( ͡° ͜ʖ ͡°)_/¯", performance_median_reading)
print(" \n ¯\_( ͡° ͜ʖ ͡°)_/¯ MODE FOR READING ¯\_( ͡° ͜ʖ ͡°)_/¯", performance_mode_reading)
print(" \n ¯\_( ͡° ͜ʖ ͡°)_/¯ STANDARD DEVIATION FOR READING ¯\_( ͡° ͜ʖ ͡°)_/¯", performance_mean_reading_std_deviation)
# 
fig2.show()
# 
print("¯\_( ͡° ͜ʖ ͡°)_/¯ MEAN FOR MATH ¯\_( ͡° ͜ʖ ͡°)_/¯", performance_mean_math)
print(" \n ¯\_( ͡° ͜ʖ ͡°)_/¯ MEDIAN FOR MATH ¯\_( ͡° ͜ʖ ͡°)_/¯", performance_median_math)
print(" \n ¯\_( ͡° ͜ʖ ͡°)_/¯ MODE FOR MATH ¯\_( ͡° ͜ʖ ͡°)_/¯", performance_mode_math)
print(" \n ¯\_( ͡° ͜ʖ ͡°)_/¯ STANDARD DEVIATION FOR MATH ¯\_( ͡° ͜ʖ ͡°)_/¯", performance_mean_math_std_deviation)
# 
fig3.show()
# 
print(" \n ¯\_( ͡° ͜ʖ ͡°)_/¯ MEAN FOR WRITING ¯\_( ͡° ͜ʖ ͡°)_/¯", performance_mean_writing)
print(" \n ¯\_( ͡° ͜ʖ ͡°)_/¯ MEDIAN FOR WRITING ¯\_( ͡° ͜ʖ ͡°)_/¯", performance_median_writing)
print(" \n ¯\_( ͡° ͜ʖ ͡°)_/¯ MODE FOR WRITING ¯\_( ͡° ͜ʖ ͡°)_/¯", performance_mode_writing)
print(" \n ¯\_( ͡° ͜ʖ ͡°)_/¯ STANDARD DEVIATION FOR WRITING ¯\_( ͡° ͜ʖ ͡°)_/¯", performance_mean_writing_std_deviation)
# 
