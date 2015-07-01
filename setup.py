from setuptools import setup, find_packages
import os

version = '1.0'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='bst.pygasus.wsgi',
      version=version,
      description="WSGI Interface for bst.pygasus",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Programming Language :: Python",
      ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['bb', 'bst.pygasus'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Paste',
          'PasteDeploy',
          'waitress',
          'transaction'
          # -*- Extra requirements: -*-
      ],
      entry_points={
          'console_scripts': ['serve = bst.pygasus.wsgi.server:run'],
          'paste.app_factory': ['main = bst.pygasus.wsgi.server:make_app',
                                'debug = bst.pygasus.wsgi.server:make_debug']
      },
      )
