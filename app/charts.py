import matplotlib.pyplot as plot


def generateBarChart(imageName, labels, values):
    figure, axis = plot.subplots()
    axis.bar(labels, values)
    plot.savefig(f"./img/{imageName}.png")
    plot.close()


def generatePieChart(label, values):
    figure, axis = plot.subplots()
    axis.pie(values, labels=label)
    axis.axis("equal")
    plot.savefig("pie.png")
    plot.close()


if __name__ == "__main__":
    labels = ["A", "B", "C", "D", "E"]
    values = [100, 200, 300, 400, 500]
    generateBarChart(labels, values)
    generatePieChart(labels, values)
