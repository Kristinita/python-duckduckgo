from duckduckgo import __version__
from setuptools import setup

long_description = open('README.MD').read()

setup(name='duckduckgo',
      version=__version__,
      py_modules=['duckduckgo'],
      description='Python 3 library for querying the DuckDuckGo API',
      author='Sasha Chernykh',
      license='BSD',
      url='https://github.com/Kristinita/python-duckduckgo',
      long_description=long_description,
      platforms=['any'],
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
                   ],
      entry_points={'console_scripts': ['ddg = duckduckgo:main']},
      zip_safe=False,
      )
