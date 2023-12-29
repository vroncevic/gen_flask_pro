Generate Flask Project
-----------------------

**gen_flask_pro** is tool for generation of flask project.

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the tool and provide instructions on
how to install the tool, any machine dependencies it may have and any
other information that should be provided before the tool is installed.

|gen_flask_pro python checker| |gen_flask_pro python package| |github issues| |documentation status| |github contributors|

.. |gen_flask_pro python checker| image:: https://github.com/vroncevic/gen_flask_pro/actions/workflows/gen_flask_pro_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_flask_pro/actions/workflows/gen_flask_pro_python_checker.yml

.. |gen_flask_pro python package| image:: https://github.com/vroncevic/gen_flask_pro/actions/workflows/gen_flask_pro_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_flask_pro/actions/workflows/gen_flask_pro_package.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_flask_pro.svg
   :target: https://github.com/vroncevic/gen_flask_pro/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_flask_pro.svg
   :target: https://github.com/vroncevic/gen_flask_pro/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen_flask_pro/badge/?version=latest
   :target: https://gen-flask-pro.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

Installation
-------------

|gen_flask_pro python3 build|

.. |gen_flask_pro python3 build| image:: https://github.com/vroncevic/gen_flask_pro/actions/workflows/gen_flask_pro_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_flask_pro/actions/workflows/gen_flask_pro_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_flask_pro/releases

To install **gen_flask_pro** type the following

.. code-block:: bash

    tar xvzf gen_flask_pro-x.y.z.tar.gz
    cd gen_flask_pro-x.y.z/
    # python3
    wget https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py 
    python3 -m pip install --upgrade setuptools
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade build
    pip3 install -r requirements.txt
    python3 -m build --no-isolation --wheel
    pip3 install ./dist/gen_flask_pro-*-py3-none-any.whl
    rm -f get-pip.py
    chmod 755 /usr/local/lib/python3.9/dist-packages/usr/local/bin/gen_flask_pro_run.py
    ln -s /usr/local/lib/python3.9/dist-packages/usr/local/bin/gen_flask_pro_run.py /usr/local/bin/gen_flask_pro_run.py

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # pyton3
    pip3 install gen_flask_pro

Dependencies
-------------

**gen_flask_pro** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
---------------

**gen_flask_pro** is based on OOP.

Tool structure

.. code-block:: bash

    gen_flask_pro/
        ├── conf/
        │   ├── gen_flask_pro.cfg
        │   ├── gen_flask_pro.logo
        │   ├── gen_flask_pro_util.cfg
        │   └── template/
        │       └── generator_test.template
        ├── __init__.py
        ├── log/
        │   └── gen_flask_pro.log
        ├── pro/
        │   ├── __init__.py
        │   ├── read_template.py
        │   └── write_template.py
        └── run/
            └── gen_flask_pro_run.py
        
        5 directories, 10 files

Copyright and licence
-----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2016 - 2024 by `vroncevic.github.io/gen_flask_pro <https://vroncevic.github.io/gen_flask_pro>`_

**gen_flask_pro** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_flask_pro/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
