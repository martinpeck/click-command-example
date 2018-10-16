from setuptools import setup

setup(
  name='SimpleClickExample',
  version='1.0',
  py_modules=['hello'],
  instal_required=[
    'Click'
  ],
  entry_points='''
    [console_scripts]
    hello=hello:cli
  '''
)