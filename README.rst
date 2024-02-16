python-jyutping
===============

Python tool to convert Chinese characters to Jyutping.

Install
-------

.. code:: bash

    $ pip install jyutping

Usage
-----

.. code:: python

    >>> import jyutping

    >>> jyutping.get('广东话')  # Python 3
    >>> jyutping.get(u'广东话')  # Python 2
    ['gwong2', 'dung1', 'waa6']
    
    >>> jyutping.get('广东话', multiple=True)
    [{'gwong2'}, {'dung1'}, {'waa6', 'waa2'}]
