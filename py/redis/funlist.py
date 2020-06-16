import csv
import redis

rc = redis.Redis(host='localhost', port=6379, db=0)

with open('/j/tmp32/bluemesa/tmp/ui-fun-20-06-16.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
