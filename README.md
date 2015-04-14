# djangocms ajax contact plugin

A djangocms ajax contact form plugin.

## Installation

* ``pip install git+ssh://git@github.com/creimers/cmsplugin_ajaxcontact.git``

* add 

  ```
  'captcha',
  'cmsplugin_ajaxcontact'
  ```

  to ``INSTALLED_APPS`` in ``settings.py``

* add ``RECAPTCHA_PRIVATE_KEY`` and ``RECAPTCHA_PUPLIC_KEY`` to ``settings.py``

* add ``CAPTCHA_AJAX = True`` to ``settings.py``

* add ``url(r'^ajax_form/', include('cmsplugin_ajaxcontact.urls', namespace='ajax_contact')),`` to ``myproject/urls.py``

* configure your django installation so it can [send mail](https://docs.djangoproject.com/en/dev/topics/email/)
