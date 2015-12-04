"""
@author - Kem Andrew
@date -  11/24/2015
@description - This program reads the nodes and edges files in, retreives
			   a geometry for a node based on the id. The geometry is printed in the
			   output.

@resources - Github repo: https://github.com/rugbyprof/load_spatial_db
"""

import csv
import json

# These lists hold node and edge data
nodes = []
edges =[]

# Dictionary to hold geometry data
geometry = {}

# Reads csv file containing nodes
with open('nodes.csv', 'rb') as csvfile:
     rows = csv.reader(csvfile, delimiter=',', quotechar='"')
     for row in rows:
         nodes.append(row)

# Reads csv file containing edges
with open('edges.csv', 'rb') as csvfile:
     rows = csv.reader(csvfile, delimiter=',', quotechar='"')
     for row in rows:
         edges.append(row)

f = open('nodegeometry.json', 'r')

for line in f:
    line = json.loads(line)
    print line['id']
    geometry[line['id']] = line['geometry']

#print len(nodes)
#print len(edges)

#print geometry[str(whatever)]
