#-*- coding:utf-8 -*-

from __future__ import absolute_import, division
import os
import argparse
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from thermocalc.models import TFurnance, Curve


def parse_sysargv():
    descr = """conversor temperatura-posición y posición-temperatura para distribuciones .curve"""
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument('curvefile', help="archivo .curve con pares [R  T]", type=str)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-t", "--temp", help="temperatura objetivo: se busca posicion correspondiente",
                        type=float)
    group.add_argument("-p", "--pos", help="posicion de entrada objetivo [mm]: se busca temperatura correspondiente",
                        type=float)
    parser.add_argument('-d', help="realiza la busqueda de la temperatura objetivo en el ala descendente de la curva",
                        action="store_true")
    return parser.parse_args()

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def biseccion(f, ttarget, a, b):
    epsilon = 1e-4
    fa, fb = f(a) - ttarget, f(b) - ttarget
    while True:
        xmed = 0.5 * (a + b)
        newf = f(xmed)

        if abs(newf - ttarget) < epsilon:
            return xmed
        else:
            if (newf - ttarget) * fb > 0.0:
                b = xmed
            else:
                a = xmed
    
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def curve_regression():
    # arguments parsing
    args = parse_sysargv()
    
    # lectura del archivo de .curve y creacion de los objetos TFurnance y Curve
    with open(args.curvefile, 'r') as data:
        ltubo = float(data.readline().replace('\n', ''))
        ltermopar = float(data.readline().replace('\n', ''))
        horno = TFurnance(ltubo, ltermopar)
        curva = Curve()
        for line in data:
            x, y = line.replace('\n', '').split(',')
            curva.add_point(float(x), float(y))
    
    # funcion de interpolacion
    f = interp1d(curva.x, curva.y, kind='cubic')
    
    # seleccion de caso
    if args.temp != None:       # si se busca la posicion correspondiente a una temperatura
        if curva.ymin <= args.temp <= curva.ymax:                           # revision de temperatura
            restemp = args.temp
            if args.d:
                Rpos = biseccion(f, restemp, curva.xmin, curva.x[curva.y.index(max(curva.y))])
            else:
                Rpos = biseccion(f, restemp, curva.x[curva.y.index(max(curva.y))], curva.xmax)
            respos = horno.R2p(Rpos)
            msg = u'{}: {}°C -> {:0.2f}mm'.format(args.curvefile.split('.')[0], restemp, respos)
            graph = True
            print u'\n    ' + msg + u'\n'
        else:
            graph = False
            print u"""\n    NO DATA: {}°C esta fuera del \
dominio de la curva: {}-{}°C\n""".format(args.temp, curva.ymin, curva.ymax)
    else:                       # si se busca la temperatura correspondiente a una posicion
        if horno.R2p(curva.xmax) <= args.pos <= horno.R2p(curva.xmin):      # revision del valor p
            restemp = float(f(horno.p2R(args.pos)))
            respos = args.pos
            msg = u'{}: {}mm -> {:0.2f}°C'.format(args.curvefile.split('.')[0], respos, restemp)
            graph = True
            print u'\n    ' + msg + u'\n'
        else:
            graph = False
            print """\n    NO DATA: {}mm (desde la entrada del tubo) esta fuera del \
dominio de la curva: {}-{}mm\n""".format(args.pos, horno.R2p(curva.xmax), horno.R2p(curva.xmin))
    
    # grafica
    if graph:
        xnew = np.linspace(curva.xmin, curva.xmax,100)
        xmod = np.linspace(horno.R2p(curva.xmin), horno.R2p(curva.xmax),100)
        plt.plot([horno.R2p(x) for x in curva.x], curva.y, 'o')
        plt.plot(xmod, f(xnew), linewidth=1.5)
        # plotting line plot([x1,x2], [y1, y2])
        plt.plot([0, respos], [restemp, restemp], 'r-', lw=1.5)
        plt.plot([respos, respos], [restemp, plt.ylim()[0]], 'r-', lw=1.5)
        plt.title(msg)
        plt.xlabel('mm desde la boca del tubo')
        plt.ylabel(u'°C')
        plt.grid()
        plt.show()
