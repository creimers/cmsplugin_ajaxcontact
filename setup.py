try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import cmsplugin_ajaxcontact

version = cmsplugin_ajaxcontact.__version__

setup(
    name = 'cmsplugin_ajaxcontact',
    packages = ['cmsplugin_ajaxcontact'],
    include_package_data = True,
    version = version,
    description = 'A djangocms plugin ajax contact form',
    author = 'Christoph Reimers',
    author_email = 'christoph@superservice-international.com',
    license='BSD License',
    url = 'https://github.com/creimers/cmsplugin_ajaxcontact',
    keywords = ['djangocms', 'django', 'ajax', 'form'], 
    install_requires = [
        'django-cms>=3.0',
        'django-recaptcha',
    ],
    classifiers = [
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Framework :: Django',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
)
