.. ssllabs documentation master file, created by
   sphinx-quickstart on Thu Jan 12 15:08:12 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

#####################
ssllabs python module
#####################

*************
What is this?
*************

Python module for easy working with the Qualys SSL Labs API. Should be fully
compatible with Python 2 and 3.  Depends on requests and six.

This API works through the remote SSL Labs servers, and information that you
pass through this API will in turn be passed to the SSL Labs servers.

The best place to start is probably at :class:`ssllabs.client.Client`.  That's
the main interface you should be using to run the API, possibly catching errors
from :mod:`ssllabs.errors`.

The sources are available in the `GitHub Repository
<https://github.com/Taywee/ssllabs>`__, and releases can be downloaded in the
`releases tab <https://github.com/Taywee/ssllabs/releases>`__

**********
Disclaimer
**********
I am not affiliated with SSL Labs or Qualys, and this project is not supported
by SSL Labs or Qualys.

*****************
Table of Contents
*****************

.. toctree::
    :maxdepth: 2

    cert
    chain
    chaincert
    client
    drownhost
    endpoint
    endpointdetails
    errors
    host
    hpkppolicy
    hstspolicy
    hstspreload
    info
    key
    object
    protocol
    simclient
    simdetails
    simulation
    statuscodes
    suite
    suites
    util

******************
Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

*******
License
*******

This module is released under the MIT license, With the additional restrictions
as specified in the `SSL Labs terms of use
<https://www.ssllabs.com/about/terms.html>`__.  If you use this module, as a
user of the SSL Labs API, you will also be bound by those restrictions.
