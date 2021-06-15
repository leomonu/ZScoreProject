from os import name
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics
import random

df  = pd.read_csv("medium_data.csv")
data = df["id"].tolist()



mean_population = statistics.mean(data)
stddv_population = statistics.mean(data)

print("Mean of the population : ",mean_population)
print("Standard Deviation of population",stddv_population)

def random_set_of_means(counter):
    dataSet = []
    for i in range(100):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    
    mean = statistics.mean(dataSet)
    return mean

meanList = []

for i in range(1000):
    setOfMean = random_set_of_means(100)
    meanList.append(setOfMean)

stddev = statistics.stdev(meanList)
mean = statistics.mean(meanList)

print("Mean of sampling distribution : ",mean)
print("Standard Deviation of sampling distribution",stddev)


firstStdDevStart,firstStdDevEnd = mean-stddev,mean+stddev
secondStdDevStart,secondStdDevEnd = mean-(2*stddev),mean+(2*stddev)
thirdStdDevStart,thirdStdDevEnd = mean-(3*stddev),mean+(3*stddev)




fig = ff.create_distplot([meanList],["id"],show_hist=False)
# fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.2],mode  = "lines",name = "Mean"))
# fig.add_trace(go.Scatter(x = [meanOfSample3,meanOfSample3],y = [0,0.2],mode = "lines",name = "Sample 3 "))
# # fig.add_trace(go.Scatter(x = [firstStdDevStart,firstStdDevStart],y = [0,0.2],mode = "lines",name = "First Standard Deviation Start"))
# fig.add_trace(go.Scatter(x = [firstStdDevEnd,firstStdDevEnd],y = [0,0.2],mode = "lines",name = "First Standard Deviation End"))
# # fig.add_trace(go.Scatter(x = [secondStdDevStart,secondStdDevStart],y = [0,0.2],mode = "lines",name = "Second Standard Deviation Start"))
# fig.add_trace(go.Scatter(x = [secondStdDevEnd,secondStdDevEnd],y = [0,0.2],mode = "lines",name = "Second Standard Deviation End"))
# # fig.add_trace(go.Scatter(x = [thirdStdDevStart,thirdStdDevStart],y = [0,0.2],mode = "lines",name = "Third Standard Deviation Start"))
# fig.add_trace(go.Scatter(x = [thirdStdDevEnd,thirdStdDevEnd],y = [0,0.2],mode = "lines",name = "Third Standard Deviation End"))




fig.show()




