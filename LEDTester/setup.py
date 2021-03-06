from setuptools import setup

setup(name='lightswitch',
      version='0.2',
      description='Program to send commands to LED board',
      author = 'Pamela Kelly',
      author_email = 'pamela.kelly@ucdconnect.ie',
      url='https://github.com/ucd2017comp30670/assignment3-PamelaKelly',
      license = 'GNU',
      packages = ['lightswitch', 'tests'],
      entry_points = {
          'console_scripts': ['lightswitch=lightswitch.main:lightswitch']
          }
      )
