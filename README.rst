===============
petLost project
===============

.. image:: https://travis-ci.org/isgroba/petlost.svg?branch=master
    :target: https://travis-ci.org/isgroba/petlost

** PetLost ** is a progressive web app. This project consist of a web in 
which you can upload information of any animal that you find lost.

This project uses Spanish as the comunication language.

Cómo colaborar en el proyecto
=============================

Base
----

- Instalar python 3.5
- Instalar y configurar git

Instalación en Mac/Linux
------------------------

.. code::

    git clone https://github.com/isgroba/petlost
    cd petlost
    python3 -m venv .venv
    source .venv/bin/activate

Una vez dentro de la máquina virtual (.venv)

.. code::

    pip install --upgrade pip setuptools wheel
    pip install pip-tools --upgrade
    pip install --requirement requirements.txt
    pip install --requirement dev-requirements.txt

Instalación en windows
----------------------

.. code::
    git clone https://github.com/isgroba/petlost
    cd petlost
    python -m venv .venv
    source .venv\Scripts\Activate.PS1

Una vez dentro de la máquina virtual (.venv)

.. code::

    pip install --upgrade pip setuptools wheel
    pip install pip-tools --upgrade
    pip install --requirement requirements.txt
    pip install --requirement dev-requirements.txt

Tests y cobertura de código
---------------------------

La calidad del código está gestionada por:
 **pytest** para ejecutar los tests del código y la cobertura:
 
 .. code::
    pytest
    pytest --cov

**flake8** lo ejecutamos para comprobar que el código sigue las recomendaciones de estilo de PEP8:

.. code::
    flake8

**isort** comprueba que los importes estén ordenados

.. code::

    isort
