import simplejson
import sys

f = open(sys.argv[1])
x = simplejson.load(f)
min_timeslot = 999999999999999
max_timeslot = -999999999999999
min_value = 999999999999999
max_value = -999999999999999

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
print (min_timeslot, max_timeslot, min_value, max_value)
g = open(sys.argv[1],'w')
simplejson.dump(x, g)
g.flush()
g.close()

#for f in *.geojson; do python aggr.py $f; done
