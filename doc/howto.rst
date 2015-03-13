Guía rápida
===========

Acontinuación encontrarás una guia rápida para el uso de los cuatro comandos que componen **ThermoCalc**:

thermocalc-raw2curve
--------------------

.. code-block:: bash

    $ thermocalc-raw2curve --help
    usage: thermocalc-raw2curve [-h] ltubo ltermopar datafile

    genera un archivo .curve con la distribución térmica de un horno tubular
    basado en las mediciones tomadas con un termopar; pares posicion temperatura.

    positional arguments:
      ltubo       longitud del tubo en [mm]
      ltermopar   longitud del termopar en [mm]
      datafile    archivo de datos [x T]

    optional arguments:
      -h, --help  show this help message and exit

    
    $ thermocalc-raw2curve 750 615 raw_data.csv

.. warning::
    
    Las dimensiones deben estar en [mm] salvo expresa indicación.

thermocalc-curveview
--------------------

.. code-block:: bash
    
    $ thermocalc-curveview -h
    usage: curvevisualizator.py [-h] curve [curve ...]

    visualiza una o mas distribuciónes térmicas con base en archivos .curve

    positional arguments:
      curve       archivo .curve con pares [R T]

    optional arguments:
      -h, --help  show this help message and exit


    $ thermocalc-curveview file1.curve file2.curve ...

thermocalc-regression
---------------------

.. code-block:: bash
    
    $ thermocalc-regression -h
    usage: thermocalc-regression [-h] (-t TEMP | -p POS) curvefile

    conversor temperatura-posición y posición-temperatura para distribuciones
    .curve

    positional arguments:
      curvefile             archivo .curve con pares [R T]

    optional arguments:
      -h, --help            show this help message and exit
      -t TEMP, --temp TEMP  temperatura objetivo: se busca posicion
                            correspondiente
      -p POS, --pos POS     posicion de entrada objetivo [mm]: se busca
                            temperatura correspondiente

    
    # temperatura-posicion 
    $ thermocalc-regression curve_file.curve --temp 900
    
    # posicion-temperatura 
    $ thermocalc-regression curve_file.curve --pos 330

thermocalc-x2p
--------------

.. code-block:: bash
    
    $ thermocalc-x2p --help
    usage: posfromcouple.py [-h] ltubo ltermopar x

    transforma una medición de termopar en una de entrada de tubo o de centro

    positional arguments:
      ltubo       longitud del tubo en [mm]
      ltermopar   longitud del termopar en [mm]
      x           longitud entre la boca del tubo y la referencia del termopar
                  [cm]

    optional arguments:
      -h, --help  show this help message and exit


    $ thermocalc-x2p 1200 650 8.5
    
.. warning::
    El valor de **x** se debe dar en [cm]
