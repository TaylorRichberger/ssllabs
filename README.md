# ssllabs
Python module for easy working with the Qualys SSL Labs API. Should be fully
compatible with Python 2 and 3.  Depends on requests and six.

This API works through the remote SSL Labs servers, and information that you
pass through this API will in turn be passed to the SSL Labs servers.

Installation of the wheel also will install a program named
`ssllabs-gradecheck`, which  may be used to run a quick test of an SSL
endpoint, and give the return status (and output text) based on user-specified
criteria.  This may be used as a part of a script for regular checking of a
certificate, to check for expiration or other issues.

# Disclaimer
I am not affiliated with SSL Labs or Qualys, and this project is not supported
by SSL Labs or Qualys.

# Documentation
The best place to access the documentation is the [GitHub Pages generated
documentation](https://taywee.github.io/ssllabs/), or by generating the
documentation yourself.

# License
This module is released under the MIT license, With the additional restrictions
as specified in the [SSL Labs terms of
use](https://www.ssllabs.com/about/terms.html).  If you use this module, as a
user of the SSL Labs API, you will also be bound by those restrictions.
