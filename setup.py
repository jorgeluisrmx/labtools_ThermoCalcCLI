#!/usr/bin/env python
#-*- coding:utf-8 -*-

from distutils.core import setup
from setuptools import find_packages

setup(
    name='ThermoCalc',
    version='1.0.0',
    author='JL Rodriguez',
    author_email='jorgeluisrmx@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'thermocalc-raw2curve = thermocalc.controllers:raw_to_curve',
            'thermocalc-curveview = thermocalc.controllers:curve_viewer',
            'thermocalc-regression = thermocalc.controllers:curve_regression',
            'thermocalc-x2p = thermocalc.controllers:pos_from_couple'
        ]},
    url='',
    license='LICENSE.txt',
    description='Conversor temperatura-posicion para hornos tubulares con interfaz en linea de comando',
    long_description=open('README.txt').read(),
    install_requires=['numpy', 'scipy', 'matplotlib'],
)
