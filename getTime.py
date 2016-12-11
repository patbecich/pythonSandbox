
import requests

r = requests.get('http://date.jsontest.com')


#print r.text

d = r.json()

print d

print d['date'],d['time']

checks = []

checks.append(d['date']+d['time'])
