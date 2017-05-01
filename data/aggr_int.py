import simplejson
import sys
import arrow

f = open(sys.argv[1])
x = simplejson.load(f)
min_timeslot = 999999999999999
max_timeslot = -999999999999999
min_value = 999999999999999
max_value = -999999999999999


x['properties'] = {}
x['type'] = 'FeatureCollection'
p = x['properties']
p['source'] = 'UNKNOWN'
p['type'] = 'CLOSENESS'
x['properties']['starttime'] = 1464732000000

print p
for feature in x['features']:
   for timeslot,value in feature['properties'].items():
       timeslot = int(timeslot)
       value = float(value)
       if timeslot < min_timeslot:
           min_timeslot = timeslot
       if timeslot > max_timeslot:
           max_timeslot = timeslot
       if value > max_value:
           max_value = value
       if value < min_value:
           min_value = value

x['properties']['min_timeslot' ] = min_timeslot
x['properties']['max_timeslot' ] = max_timeslot
x['properties']['min_value' ] = min_value
x['properties']['max_value' ] = max_value

x['properties']['min_value' ] = min_value-0.00000000000001
x['properties']['max_value' ] = max_value+0.00000000000001
if x['properties']['starttime'] == 1464804000000:
    x['properties']['starttime'] = 1464732000000
print x['properties']

for i in range(min_timeslot,max_timeslot):
  dt = arrow.get((x['properties']['starttime']/1000) + i*3600).to('Europe/Amsterdam')
  if dt.hour == 0:
      key = 'day_'+str(dt.weekday())
      if key not in x['properties']:
          x['properties'][key] = i

print x['properties']


print (min_timeslot, max_timeslot, min_value, max_value)
g = open(sys.argv[1],'w')
simplejson.dump(x, g)
g.flush()
g.close()

#for f in *.geojson; do python aggr.py $f; done
