from setuptools import setup

setup(
  name="paquetecalculos",
  version="1.0",
  description="Esto es un paquete de prueba",
  author="Caros granada",
  author_email="carlosgranadacra@gmail.com",
  packages=["calculos","calculos.calculos_generales"]

)
#Crear paquete -> python setup.py sdist
#Intalar > pip3 install paquete
#Desistalar -> pip3 unistall npmbre-paquete