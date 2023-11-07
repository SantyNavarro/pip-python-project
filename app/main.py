import utils
import readCSV
import charts
import pandas as pd


def run():
    """
    data = readCSV.readCSV("data.csv")
    countries = list(map(lambda x: x["Country/Territory"], data))
    percentagesByCountry = list(map(lambda x: x["World Population Percentage"], data))
    charts.generatePieChart(countries, percentagesByCountry)
    """

    dataFrames = pd.read_csv("data.csv")
    dataFrames = dataFrames[dataFrames["Continent"] == "Europe"]
    countries = dataFrames["Country/Territory"].values
    percentagesByCountry = dataFrames["World Population Percentage"].values
    charts.generatePieChart(countries, percentagesByCountry)

    data = readCSV.readCSV("data.csv")
    country = input("Type the country´s name: ")
    result = utils.populationByCountry(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.getPopulation(country)
        charts.generateBarChart(country["Country/Territory"], labels, values)


if __name__ == "__main__":
    run()
