# Practica Sphinx

simepre hay que estar dentro den (.venv) 


comando para iniciar sphinx ` sphinx-quickstart`

ahora haríamos un `sphinx-apidoc -o source ./source`


archivo conf.py dentro de la carpeta source

```Python
# añadimos los imports:
import os
import sys

sys.path.insert(0, os.path.abspath(''))

# modificamos el archivo extensions añadiendo lo ssiguiente
extensions = [
    'sphinx.ext.autodoc',
    
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
]

```

 `sphinx-build source build`  

dentro del archivo source debemos tener nuestro proyecto.py comentado:
y en el archivo index.rst
indicamos los archivos que tenemos comentados
``` rst
Welcome to practicaExamen12-3-24's documentation!
=================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Factura

```
al abrir el index.html dentro de la carpeta build ya estaría