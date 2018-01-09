### 1. Description

This is the version of [**python-duckduckgo**](https://github.com/crazedpsyc/python-duckduckgo) module, ported for Python 3. What is it, and how you can use it, see [**in original README**](https://github.com/crazedpsyc/python-duckduckgo/blob/master/README.rst).

### 2. Testing environment

This module successful works for me in:

+ Windows 10 Enterprise LTSB 64-bit
+ Python 3.3 or Python 3.6.4 environment.

Must worked in another operation systems and Python 3 versions.

### 3. Installation

+ `pip install git+https://github.com/Kristinita/python-duckduckgo`

### 4. Comparison with the original module

I did the following procedures:

1. `2to3 -w duckduckgo.py`,
1. Add `.decode('UTF-8')` [**as in this comment**](https://stackoverflow.com/questions/43026384/duckduckgo-module-not-working-in-python-3-4-4#comment74208974_43064869).

