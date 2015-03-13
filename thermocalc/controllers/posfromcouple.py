#-*- coding:utf-8 -*-

from __future__ import absolute_import
import argparse
from thermocalc.models import TFurnance


def parse_sysargv():
    descr = """transforma una medición de termopar en una de entrada de tubo o de centro"""
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument('ltubo', help="longitud del tubo en [mm]", type=float)
    parser.add_argument('ltermopar', help="longitud del termopar en [mm]", type=float)
    parser.add_argument('x',
            help="longitud entre la boca del tubo y la referencia del termopar [cm]", type=float)
    return parser.parse_args()
    
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def pos_from_couple():
    # arguments parsing
    args = parse_sysargv()
    
    # creacion de modelo goemtrico del horno
    horno = TFurnance(args.ltubo, args.ltermopar)
    
    # salida
    print
    print " {}cm (de termopar) -> {}mm desde la boca del tubo".format(args.x, horno.x2p(args.x))
    print
