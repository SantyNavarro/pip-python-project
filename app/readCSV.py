import csv

def readCSV(path):
  with open(path, 'r') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    header = next(reader)
    countriesDictionary = []
    for row in reader:
      iterable = zip(header, row)
      dataSet = {column: row for column, row in iterable}
      countriesDictionary.append(dataSet)
    return countriesDictionary  

if __name__ == '__main__':
  dataSet = readCSV('./app/data.csv')
  print(dataSet)