#-*- coding:utf-8 -*-

from __future__ import absolute_import

class Curve(object):
    """
    Modelo encargado del almacenamiento de los datos R,T para
    una curva termica a TMax
    """
    
    
    def __init__(self):
        """
        Constructor de clase Curve
        
        :rtype: void
        """
        self._x = []
        self._y = []
    
    
    def __iter__(self):
        """
        Define a los objetos de clase Curve como iterables
        y regresa la lista de coordenadas en una iteracion
        
        :rtype: Curve
        """
        return ( (x,y) for x, y in zip(self._x, self._y) )
    
    
    def __repr__(self):
        """
        Representacion en string del objeto de clase Curve
        
        :rtype: str
        """
        if len(self._x) == 0 or len(self._y) == 0:
            return 'empty Curve'
        return '\n'.join( [ (str(x) + ', ' + str(y)) for x, y in zip(self._x, self._y)] )


    @property
    def x(self):
        """
        Getter para los valores x de la lista
        
        :rtype: list
        """
        return self._x
    
    
    @property
    def y(self):
        """
        Getter para los valores y de la lista
        
        :rtype: list
        """
        return self._y
    
    @property
    def xmin(self):
        """
        Getter para el valor minimo de x
        
        :rtype: float
        """
        return self._x[0]
    
    @property
    def xmax(self):
        """
        Getter para el valor maximo de x
        
        :rtype: float
        """
        return self._x[-1]
    
    @property
    def ymin(self):
        """
        Getter para el valor minimo de y
        
        :rtype: float
        """
        return min(self._y)
    
    @property
    def ymax(self):
        """
        Getter para el valor maximo de y
        
        :rtype: float
        """
        return max(self._y)
    
    
    def add_point(self, x, y):
        """
        Agrega un nuevo punto a al final de la curva
        
        :param x: valor x
        :param y: valor y
        :rtype: void
        """
        self._x.append(x)
        self._y.append(y)
    
    
    def add_simetry(self):
        """
        Crea simetria de la curva con respecto al eje y. Teniendo una curva
        tipo [(3,30), (2,20), (1,10), (0,1)]
        se obtiene [(-3,30), (-2,20), (-1,10), (0,1), (1,10), (2,20), (3,30)]
        se amplia la curva actual, no se genera una nueva
        
        :rtype: void
        """
        new_x = [x for x in self._x[:-1]]
        new_y = [y for y in self._y[:-1]]
        new_x.reverse()
        new_y.reverse()
        self._x = [-x if x != 0 else x for x in self._x]
        self._x.extend(new_x)
        self._y.extend(new_y)
