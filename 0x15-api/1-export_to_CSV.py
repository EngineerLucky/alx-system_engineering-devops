#!/usr/bin/python3
"""
    Exports api data in the CSV format.
"""

import sys
import requests
import csv

if __name__ == "__main__":
    id = sys.argv[1]
    usrurl = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    tdsurl = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    u = requests.get(usrurl).json()

    do = requests.get(tdsurl).json()

    with open('{}.csv'.format(id), 'w') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for t in do:
            row = [id, u.get("username"), t.get("completed"), t.get("title")]
            row = [str(value) for value in row]
            csv_writer.writerow(row)
