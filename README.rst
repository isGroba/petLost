===============
petLost project
===============

.. image:: https://travis-ci.org/isGroba/petLost.svg?branch=master
    :target: https://travis-ci.org/isGroba/petLost

**PetLost** is a progressive web app. This project consists of
a web where you can upload information of any animal you
find in the street or that you have lost.
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

Montar base de datos
--------------------

Instalar postgres9.5 y a continuación crear el usuario y la base de datos iniciales:

.. code::

    CREATE DATABASE petlost;

    CREATE USER pet PASSWORD 'petlost';

Una vez hecho esto tenemos que cargar las migraciones de la base de datos:

.. code::

    python3 manage.py migrate

Para cargar los colores de la base de datos:

.. code::

    python3 manage.py sampledata

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

