======================
certbot-helpers-apache
======================
This respository contains a small collection of shell scripts and Python scrips
you an use to further automate the use of certbot with Apache.

Note that you need to install the following package (on Ubuntu) to use these
tools:

* certbot
* python3-certbot-apache

The provides files should be copied into /etc/letsencrypt/ prior to use.
Alternately, you can place them in other locations provided you update
``renew_certificates.service`` to point to the files in the new location.


create_certificate
==================
This small script will scan your Apache2 configuration identifying virtual
hosts on your system.  The script will then run certbot to obtain a certificate
that can be used with those hosts.


renew_certificates
==================
We've found that certbot's automatic renewal feature is problematic.  To work
around the issues, we've created our own renewal system that you can run on
your system.

Copy the ``renew_certificates.service`` file into ``/etc/systemd/system/``
and enable the certificate renewal system by running:

.. code-block:: bash

   sudo systemctl enable renew_certificates
   sudo systemctl start renew_certificates

The certificate renewal system will once at random intervals, on average, once
daily to check and, if needed, renew your certificates.

You can manually renew certificates by running the ``renew_certificates`` shell
script.
