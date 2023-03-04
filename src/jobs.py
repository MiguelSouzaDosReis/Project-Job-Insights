import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        data = list(csv.DictReader(file, delimiter=",", quotechar='"'))
        # listOfJobs = []
        # for row in data:
        #     listOfJobs.append(row)
        # print(data)
    return data
