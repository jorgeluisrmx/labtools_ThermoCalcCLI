Guía rápida
===========

Acontinuación encontrarás una guia rápida para el uso de los cuatro comandos que componen **ThermoCalc**:

thermocalc-raw2curve
--------------------

.. code-block:: bash

    $ thermocalc-raw2curve <longtubo> <longtermopar> raw_data.csv
    
    $ thermocalc-raw2curve 750 615 raw_data.csv

.. warning::
    
    Las dimensiones deben estar en [mm] salvo expresa indicación.

thermocalc-curveview
--------------------

.. code-block:: bash

    $ thermocalc-curveview file1.curve file2.curve ...

thermocalc-regression
---------------------

.. code-block:: bash
    
    # temperatura-posicion 
    $ thermocalc-regression curve_file.curve <target_temp> -p 
    $ thermocalc-regression curve_file.curve 900 -p 
    
    # posicion-temperatura 
    $ thermocalc-regression curve_file.curve <target_intake_pos> -t 
    $ thermocalc-regression curve_file.curve 330 -t

thermocalc-x2p
--------------

.. code-block:: bash
    
    $thermocalc-x2p <longtubo> <longtermopar> <temp> <x>
    
    $thermocalc-x2p 1200 650 1050 8.5
    
.. warning::
    El valor de **x** se debe dar en [cm]
