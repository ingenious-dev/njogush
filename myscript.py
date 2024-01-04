# import subprocess
import os
import sys

from django.core.management import execute_from_command_line
from art import *
# from daphne.management.commands import runserver
import daphne_runserver as runserver

from manage import main
# from image_to_ascii import image_to_ascii


# <<<<<<>>>>>
# COMPUTER TEXT ART

# OPTION 1
# image_to_ascii('build.png', True)

# OPTION 2
# TODO https://pypi.org/project/art/
tprint("njogush") # print ASCII text (default font) 
# ! <<<<<<>>>>>

# <<<<<<<>>>>>>
# ! SUSPENDED - even if you get daphne to work (for example by copying the executable - daphne.exe)
# ! it exhibits some hardcoding which make it impractical for distrubution to other users
# ! 2024.01.02 - https://github.com/josuhudu
# OPTION 1
# subprocess.run('daphne njogush.asgi:application')
# TODO https://github.com/django/daphne?tab=readme-ov-file#running
# TODO https://stackoverflow.com/questions/3022013/windows-cant-find-the-file-on-subprocess-cally
# subprocess.run('daphne -p 6564 njogush.asgi:application', shell=True)

# OPTION 2
# Inspired by manage.py
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'njogush.settings')

    sys.argv = ['myscript.py', 'migrate']
    execute_from_command_line(sys.argv)   

    # TODO https://docs.python.org/3/library/sys.html#sys.argv
    sys.argv = ['myscript.py', 'runserver', '0.0.0.0:6564', '--noreload']
    # execute_from_command_line(sys.argv) # This does not utilize daphne development server
    # ? WARNING - This required a deep dive into the django source code
    # ? This use is not in the 'browsable' documentation
    runserver.Command().run_from_argv(sys.argv)
# ! <<<<<<<>>>>>>