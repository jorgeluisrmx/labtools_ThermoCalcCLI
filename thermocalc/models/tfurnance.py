#-*- coding:utf-8 -*-

from __future__ import absolute_import, division


class TFurnance(object):
    """
    Clase encaragda de almacenar los datos geometricos de un horno
    tubular y proporcionar mecanismos de conversion entre dimensiones
    de termopar (x [cm]), de centro (R [mm]) y de entrada de tubo (p [mm])
    """


    def __init__(self, ltu, lte):
        """
        Constructor de la clase RawCurveConverter
        
        :param ltu: longitud del tubo en [mm]
        :param lte: lonfitud del termopar en [mm]
        :rtype: void
        """
        self.ltu = ltu
        self.lte = lte


    def x2p(self, xval):
        """
        Convierte una medidad de termopar (x [cm]) a una medida
        de entrada de tubo (p [mm])
        
        :param xval: longitud medida sobre termopar en [cm] desde la entrada del tubo
        :rtype: float 
        """
        return self.lte - 10 * xval

    
    def p2x(self, pval):
        """
        Convierte una medida de entrada de tubo (p [mm]) a una medida
        de termopar (x [cm])
        
        :param pval: longitud medida desde la entrada del tubo en [mm]
        :rtype: float
        """
        return (self.lte - pval) / 10

    
    def x2R(self, xval):
        """
        Convierte una medidad de termopar (x [cm]) a una medida
        de centro de tubo (R [mm])
        
        :param xval: longitud medida sobre termopar en [cm] desde la entrada del tubo
        :rtype: float 
        """
        return 0.5 * (self.ltu - 2 * self.lte) + 10 * xval

    
    def R2x(self, Rval):
        """
        Convierte una medida de centro de tubo (R [mm]) a una medida
        de termopar (x [cm])
        
        :param Rval: longitud medida desde el centro del tubo en [mm]
        :rtype: float
        """
        return ( Rval - 0.5 * (self.ltu - 2 * self.lte) ) / 10
