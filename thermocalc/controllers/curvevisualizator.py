#-*- coding:utf-8 -*-

from __future__ import absolute_import
import sys
import argparse
import matplotlib.pyplot as plt
from thermocalc.models import Curve


def parse_sysargv():
    descr = """visualiza una o mas distribuciónes térmicas con base en archivos .curve"""
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument('curve_files', metavar='curve', help="archivo .curve con pares [R  T]",
                        nargs='+', type=str)
    return parser.parse_args()
    
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def curve_viewer():
    # arguments parsing
    args = parse_sysargv()

    # creacion de la lista de curvas
    curvas = []
    try:
        # para cada archivo de curva
        for file_name in args.curve_files:
            # se crea un nuevo ibjeto curva en la lisra
            curvas.append(Curve())
            # se llna con los datos correspondientes
            with open(file_name, 'r') as curve_data:
                curve_data.readline()
                curve_data.readline()
                for line in curve_data:
                    x, y = line.replace('\n', '').split(',')
                    curvas[-1].add_point(float(x), float(y))
    except:
        print 'Archivo de datos "{}" NO VALIDO'.format(file_name) 
        print sys.exc_info()
        return
    
    # comienza graficacion de curvas
    for curva in curvas:
        plt.plot(curva.x, curva.y, linewidth=1.5)
    plt.grid()
    plt.xlabel('R [mm]')
    plt.ylabel(u'°C')
    plt.legend([name.split('.')[0] for name in args.curve_files], loc='best')
    plt.show()
    
