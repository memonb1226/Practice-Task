import yaml
import csv
import numpy as np
import matplotlib.pyplot as plt

def main():
    CONFIG =  yaml.load(open('config_global.yaml', 'rU'))
    x_coor = []
    y_coor = []
    
    with open('%s/data.csv' % CONFIG['build']['draw_data']) as csvfile:
        r = csv.reader(csvfile)
        for row in r:
            x_coor.append(float(row[0]))
            y_coor.append(float(row[1]))
            
    plt.scatter(x_coor, y_coor, s = 1)
    plt.savefig('%s/plot.eps' % CONFIG['build']['plot'])

main()
