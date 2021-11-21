HTML Whitespace remover for Django
==================================
|Pepy.tech Badge| |PyPi Version Badge| |Python Versions Badge| |License Badge| |Code Style|

.. |Pepy.tech Badge| image:: https://static.pepy.tech/personalized-badge/django-strip-whitespace?period=week&units=international_system&left_color=grey&right_color=orange&left_text=Downloads
   :target: https://pepy.tech/project/django-strip-whitespace

.. |PyPi Version Badge| image:: https://badge.fury.io/py/django-strip-whitespace.svg
    :target: https://badge.fury.io/py/django-strip-whitespace

.. |Python Versions Badge| image:: https://img.shields.io/pypi/pyversions/django-strip-whitespace
    :alt: PyPI - Python Version
    :target: https://github.com/baseplate-admin/django_strip_whitespace/blob/main/setup.py

.. |License Badge| image:: https://img.shields.io/pypi/l/django-strip-whitespace
   :alt: PyPI - License
   :target: https://github.com/baseplate-admin/django_strip_whitespace/blob/main/LICENSE
   
.. |Code Style| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :alt: Code Style
   
Introduction :
--------------
A powerful tool to optimize HTML

Why use "django_stip_whitespace" ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*   Adds line break to InlineJS.
*   It can automagically minify inline CSS, JS.
*   Removes <!--prettier-ignore--> from HTML.
*   It speeds up website by reducing the HTML size.
*   It compiles regex at runtime. So it's blazing fast.
*   Can be used with 'django.middleware.gzip.GZipMiddleware'.
*   Its mostly based on C ( gzip ) and Rust ( `minify-html <https://pypi.org/project/minify-html/>`__  ) libraries.
*   Significantly lower bytes transferred when working with frameworks like AlpineJs ( Almost fully working & Please open a issue in the `Issue Tracker <https://github.com/baseplate-admin/django_strip_whitespace/issues>`__ if you encounter any bug) & Petite Vue.
*   Is very customizable. ( You can configure lower level `minify-html <https://github.com/wilsonzlin/minify-html/blob/master/python/src/lib.template.rs/>`_ rust bindings and also the lower level `python <https://github.com/juancarlospaco/css-html-js-minify/blob/master/css_html_js_minify/html_minifier.py/>`_ bindings from settings.py )


Why souldn't you use django_stip_whitespace ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*   Adds unnecessary ';;' in HTML. ( If you know any regex to fix this please put a pull request )

*   Although I tried my best to use Compiled Language for Optimizations. It can still be sub miliseconds ( > 0.001 ) slower compared to normal Django Rendering. ( If you know any way to improve performance, please put a pull request )


Requirements :
--------------

*    minify-html
*    Django > 3 ( Should work with version 2? )
*    Python 3 ( Should work with all version? )
*    Brotli ( or BrotliPy ) | ( Optional )
*    ZSTD ( Optional ) 

User guide :
============

Installation :
--------------

Install with pip from pypi (No extra dependencies)::

      $ python -m pip install django_strip_whitespace

Install with pip with Brotli support::

      $ python -m pip install django_strip_whitespace[brotli]

Same but with Zstandard support::

      $ python -m pip install django_strip_whitespace[zstd]




Install with pip from github ( Development | Not Recommended for Production )::
    
      $ python -m pip install https://codeload.github.com/baseplate-admin/django_strip_whitespace/zip/refs/heads/main


Then include it in your django project:
   
   .. code-block:: python
   
        MIDDLEWARE = [
           ...
           "strip_whitespace.middlewares.HtmlStripWhiteSpaceMiddleware.html_strip_whitespace",
        ]

Or if you like:
   
   .. code-block:: python
   
        MIDDLEWARE += "strip_whitespace.middlewares.HtmlStripWhiteSpaceMiddleware.html_strip_whitespace"

Customization :
===============

Change Lower Level Bindings :
-----------------------------

Rust :
~~~~~~

The module allows `rust <https://github.com/wilsonzlin/minify-html>`_ minifier options to be changed from Django's settings.py file. If you would like to change any settings, refer to `minify-html's <https://github.com/wilsonzlin/minify-html/blob/master/python/src/lib.template.rs/>`_ source code.


The bindings are ( by default set to True ):

    .. code-block:: python

        STRIP_WHITESPACE_RUST_DO_NOT_MINIFY_DOCTYPE, # passes do_not_minify_doctype to minify-html
        STRIP_WHITESPACE_RUST_ENSURE_SPEC_CONPLIANT_UNQUOTED_ATTRIBUTE_VALUES, # passes ensure_spec_compliant_unquoted_attribute_values to minify-html
        STRIP_WHITESPACE_RUST_KEEP_CLOSING_TAGS, # passes keep_closing_tags to minify-html
        STRIP_WHITESPACE_RUST_KEEP_COMMENTS, # passes keep_comments to minify-html
        STRIP_WHITESPACE_RUST_KEEP_HTML_AND_HEAD_OPENING_TAGS, # passes keep_html_and_head_opening_tags to minify-html
        STRIP_WHITESPACE_RUST_KEEP_SPACES_BETWEEN_ATTRIBUTES, # passes keep_spaces_between_attributes to minify-html
        STRIP_WHITESPACE_RUST_MINIFY_CSS, # passes minify_css to minify-html
        STRIP_WHITESPACE_RUST_MINIFY_JS, # passes minify_js to minify-html
        STRIP_WHITESPACE_RUST_REMOVE_BANGS, # passes remove_bangs to minify-html
        STRIP_WHITESPACE_RUST_REMOVE_PROCESSING_INSTRUCTIONS, # passes remove_processing_instructions to minify-html

If you would like to change any of the above variables, simply put them in settings.py ( Please note that every variable here is a python boolean ).

For example:

    .. code-block:: python

        # settings.py

        STRIP_WHITESPACE_RUST_DO_NOT_MINIFY_DOCTYPE = False

Python :
~~~~~~~~

The module allows python minifier options to be changed from Django's settings.py file. If you would like to change any settings, refer to `python-module's <https://github.com/juancarlospaco/css-html-js-minify/blob/master/css_html_js_minify/html_minifier.py/>`_ source code.

The bindings are ( by default set to a sane value ):

    .. code-block:: python

        STRIP_WHITESPACE_PYTHON_REMOVE_COMMENTS, # False | removes comments from HTML using python ( not recommended cause rust can do that just fine and fast )
        STRIP_WHITESPACE_PYTHON_CONDENSE_STYLE_FROM_HTML, # True | replaces '<style text/css>' -> '<style>'
        STRIP_WHITESPACE_PYTHON_CONDENSE_SCRIPT_FROM_HTML, # True | replaces '<script text/javascript>' -> '<script>'
        STRIP_WHITESPACE_PYTHON_CLEAN_UNNEEDED_HTML_TAGS, # True | removes some unnecessary tags
        STRIP_WHITESPACE_PYTHON_CONDENSE_HTML_WHITESPACE, # True | This is where the magic happens.
        STRIP_WHITESPACE_PYTHON_UNQUOTE_HTML_ATTRIBUTES, # True | This is also a magic module.
       

If you would like to change any of the above variables, simply put them in settings.py ( Please note that every variable here is a python boolean )

For example:

    .. code-block:: python

        # settings.py

        STRIP_WHITESPACE_PYTHON_REMOVE_COMMENTS = True 

Change Ignored Paths :
----------------------

This module allows dynamic ignored path allocation.
So for example if your sitemap.xml is at url '/sitemap.xml' and you want to avoid minifying it ( Because this module in lower level is meant to minify HTML not XML ).
Then you can add it to ignored path. ( By default it ignores '/sitemap.xml' ) 

To customize ignored path:

    .. code-block:: python
        
        # settings.py

        STRIP_WHITESPACE_MINIFY_IGNORED_PATHS.append("/robots.txt") # Note that STRIP_WHITESPACE_MINIFY_IGNORED_PATHS is a Python List

Change NBSP Mangle Character :
------------------------------

This module first replaces the &nbsp; character from html with a character. 
For example &nbsp; becomes 'অ' ( I picked 'অ' because its a foreign character and not many sites use the character like this 'অ' ).
If for some reason this character is causing problem in your HTML. You can change this from settings.py .

To change &nbsp; mangle character:

    .. code-block:: python

        # settings.py

        # Keep the string as  short as possible.
        # If you make it long,
        # the python str.replace() method will use more CPU and RAM thus slowing your site down.
        
        STRIP_WHITESPACE_NBSP_MANGLE_CHARACTER = 'ga' # Note that STRIP_WHITESPACE_NBSP_MANGLE_CHARACTER is a python string


Contributing :
==============
If you like this project add a star. 
If you have problems or suggestions please put them in the `Issue Tracker <https://github.com/baseplate-admin/django_strip_whitespace/issues>`__.
If you like to add features. Fork this repo and submit a Pull Request. 😛

Roadmap :
=========
You tell me. If i have free time, I will implement it.
