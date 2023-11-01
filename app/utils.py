def getPopulation(countriesDictionary):
  populationRecords = {
    "1970": int(countriesDictionary['1970 Population']),
    "1980": int(countriesDictionary['1980 Population']),
    "1990": int(countriesDictionary['1990 Population']),
    "2000": int(countriesDictionary['2000 Population']),
    "2010": int(countriesDictionary['2010 Population']),
    "2015": int(countriesDictionary['2015 Population']),
    "2020": int(countriesDictionary['2020 Population']),
    "2022": int(countriesDictionary['2022 Population']),
  }
  labels = populationRecords.keys()
  values = populationRecords.values()
  return labels, values

def populationByCountry(data: list, country: str):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result