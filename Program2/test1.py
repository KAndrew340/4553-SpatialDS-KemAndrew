import sys
sys.path.append('Program Files (x86)/Graphviz2.38/bin')
import graphviz as gv
g1 = gv.Graph(format='svg')
g1.node('A')
g1.node('B')
g1.edge('A', 'B')
print(g1.source)
#g1.render(filename= 'Simple', view = True) 