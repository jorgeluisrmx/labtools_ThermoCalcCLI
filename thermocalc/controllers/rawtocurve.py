#-*- coding:utf-8 -*-

from __future__ import absolute_import
import os
import sys
import argparse
from thermocalc.models import TFurnance, Curve


def parse_sysargv():
    descr = """genera un archivo .curve con la distribución térmica de un horno tubular
basado en las mediciones tomadas con un termopar; pares posicion temperatura."""
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument('ltubo', help="longitud del tubo en [mm]", type=float)
    parser.add_argument('ltermopar', help="longitud del termopar en [mm]", type=float)
    parser.add_argument('datafile', help="archivo de datos [x   T]", type=str)
    return parser.parse_args()
    
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def raw_to_curve():
    # arguments parsing
    args = parse_sysargv()
    
    # creacion de modelo goemtrico del horno
    horno = TFurnance(args.ltubo, args.ltermopar)

    # creacion de la curva con los datos del archivo [x T]
    curva = Curve()
    try:
        with open(args.datafile, 'r') as data:
            for line in data:
                x, y = line.replace('\n', '').split('	')
                curva.add_point(horno.x2R(float(x)), float(y))
        # se agrega el ala simetrica a la curva
        curva.add_simetry()
    except:
        print 'Archivo de datos "{}" NO VALIDO'.format(args.datafile) 
        print sys.exc_info()
        return
    
    # generacion del archivo .curve
    file_name = args.datafile.split('.')[0] + '.curve'
    with open(file_name, 'w') as target:
        target.write('{}\n'.format(args.ltubo))
        target.write('{}\n'.format(args.ltermopar))
        for x, y in curva:
            target.write('{},{}\n'.format(x, y))
    print '   archivo {} generado con exito'.format(file_name)
