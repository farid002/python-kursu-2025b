"""
Virtual Environments

activate - deactivate

Win:
venv\Scripts\activate
deactivate

Unix (Linux, Mac):
source venv/bin/activate
deactivate
"""

"""
requirements.txt
"""
import os
import sys
import math
import datetime
import flask
import django
import pandas
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
"""
import pyfiglet
ascii_art = pyfiglet.figlet_format("Hello World")
print(ascii_art)
"""


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
match case
"""

"""
month = 5
match month:
    case 1:
        print("January")
    case 5:
        print("February")
    case _:
        print("No Match")
"""
