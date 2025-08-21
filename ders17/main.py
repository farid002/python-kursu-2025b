# kitabxanasiz

a = str(10)
b = 785.5205
len(a)
round(b, 2)

# python ozu ile gelen kitabxanalari
import math
import os
import sys
import datetime

import numpy
import pandas


"""
PYTHON


Proyekt A (Youtubea video yukleyen)  - numpy 1.0.0  pandas 1.5.2 youtube 5.0.2      PythonVenv1
Proyekt B  - numpy 5.0.0  tiktok 5.2.0 open-xlsx 2.0                                PythonVenv2
Proyekt C  - numpy 3.0.0  open-gpt 3.0.0                                            PythonVenv3
"""











"""
Virtual Environments

activate - deactivate

Win:
venv\Scripts\activate          - aktivleshdirmek
deactivate                     - deaktivleshdirmek

Unix (Linux, MacOS):
source venv/bin/activate
deactivate
"""

"""
requirements.txt
"""


"""
import os
import sys
import math
import datetime
import flask
import django
import pandas
"""

"""
Package:
install - pip install <pkg>
    specific version
uninstall - pip uninstall <pkg>
upgrade - pip install --upgrade <pkg>
show - pip show <pkg>
"""

"""
Other:

pip list
pip freeze
pip --help
pip --version
"""

"""
pip freeze > requirements.txt
"""

"""
pip list --outdated
"""

"""
Maraqli kitabxanalar
"""

"""
pip install pyfiglet
"""

import pyfiglet
import math
ascii_art = pyfiglet.figlet_format("Salam Xosh Geldiniz")
print(ascii_art)


"""
pip install randfacts
"""
"""
import randfacts
print(randfacts.get_fact())
"""

"""
pip install faker
"""
"""
from faker import Faker
fake = Faker()
print(fake.name())
print(fake.email())
"""

"""
import
as
*
from
venv
requirements.txt
"""
import math
from math import pi, sin, cos
import pandas as pd


# from math import factorial

"""
match case
"""


month = 5

if month == 1:
    print("January")
elif month == 5:
    print("May")
else:
    print("No Match")

# alternativi :

match month:
    case 1:
        print("January")
    case 5:
        print("May")
    case _:
        print("No Match")

