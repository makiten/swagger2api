**************
swagger2client
**************

A command line tool to convert Swagger UI files to a simple, usable library for any kind of application.

Table of Contents
#################

1. `Why?`_

2. `Getting Started`_

    * `Installation via pip`_

    * `Installation via GitHub`_

    * `Installation via apt`_

3. `Features`_

4. `Development`_

5. `TODO`_

6. `License`_

7. `Credits`_


Why?
####

I spent most of my time manually creating clients using Swagger files from whatever HTTP API I'm using. A lot
of the time, I needed to organize files specifically, so I didn't bother considering automating the task.

It turns out I wasn't alone, and other organizations built an ``api``-type module when connecting frontend apps
(e.g. with Vue) to web services. Most commonly, I see one single file for working with an API, and thus grew
the idea of ingesting a Swagger file to output a file that allows you to call app-native functions/methods in an app
to interface with an... interface.

``swagger-codegen`` is a great way to generate a client. I made this to generate a simpler client that I could import
easily into a Vue project. You can check it out `here <https://github.com/swagger-api/swagger-codegen>`_.

Getting Started
###############

Installation via pip
********************

``swagger2api`` should be available via `pip <https://pypi.org/project/pip/>`_:
::

    pip install --user swagger2api

Installation via GitHub
***********************

You can install ``swagger2client`` with the following command to get it straight from GitHub:
::

    curl -o- blahblahblah.sh | bash

Installation via apt
********************

Coming soon!

Features
########

- Can generate code in the following languages:

    + JavaScript (assumes you're using `axios <https://github.com/axios/axios>`_)

- Extensible to easily include new languages

Development
###########

If you would like to add more adapters (i.e., languages to export to) or improve anything, fork and clone your repo,
and make a PR.

Specifically on adapters, every adapter should use this specific namespace ``swagger2client.adapters.<tool name>``. It
should also have a ``convert`` method that returns ``str``. Example coming soon.

TODO
####

- Add tests

License
#######

This project is licensed under the MIT License. Feel free to modify and use how you want!

Credits
#######

* `makiten <dw@angk.org>`_