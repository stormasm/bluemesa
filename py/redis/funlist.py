import csv
import redis

rc = redis.Redis(host='localhost', port=6379, db=0)

with open('/j/tmp32/bluemesa/tmp/ui-fun-20-06-16.csv', newline='') as csvfile:
    funreader = csv.reader(csvfile, delimiter=',')
    for row in funreader:
        #print(', '.join(row))
        print(row[0],row[2])
