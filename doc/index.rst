.. ThermoCalc documentation master file, created by
   sphinx-quickstart on Wed Feb 25 06:56:46 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ThermoCalc's documentation!
======================================

ThermoCalc es un conversor temperatura-posicion para hornos tubulares con interfaz en linea de comando. Por la naturaleza del proceso, éste se encuentra dividido en cuatro componentes que se detallan más adelante. A continuación encontrarás la descripción de los términos utilizadas para referrirnos a los tres diferentes tipos de mediciones de interés:  

===============     ===================================
Medición            Descripción
===============     ===================================
de termopar (x)     | longitud entre la boca del tubo 
                    | y la referencia del termopar
de centro (R)       | longitud entre el centro del tubo
                    | y una posición interna dada
de entrada (p)      | longitud entre la boca del tubo
                    | y una posición interna dada
===============     ===================================

Comandos disponibles
--------------------

=====================   =============================================
Componente              Descrición
=====================   =============================================
thermocalc-raw2curve    | genera un archivo *.curve* con la 
                        | distribución térmica de un horno tubular 
                        | basado en las mediciones tomadas con 
                        | un termopar; pares posicion temperatura.            
thermocalc-curveview    | visualiza una o mas distribuciónes térmicas
                        | con base en archivos *.curve*                       
thermocalc-regression   | conversor temperatura-posición y
                        | posición-temperatura para distribuciones                   
                        | *.curve*                        
thermocalc-x2p          | transforma una medición de termopar en una
                        | de entrada de tubo o de centro
=====================   =============================================


Contents:
---------

.. toctree::
   :maxdepth: 2
   
   howto
   models
   controllers
   views
    


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

