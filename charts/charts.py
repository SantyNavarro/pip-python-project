import matplotlib.pyplot as pyplot


def generatePieChart():
    labels = ["A", "B", "C"]
    values = [200, 34, 120]
    figure, axis = pyplot.subplots()
    axis.pie(values, labels=labels)
    pyplot.savefig("pie.png")
    pyplot.close()
