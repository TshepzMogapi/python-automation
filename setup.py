from setuptools import setup, find_packages

def get_requirements():
  with open('requirements.txt', 'r') as req:
    contents = req.read()
    requirements = contents.split('\n')

    return requirements

setup(
  name='tm',
  version='0.0.1',
  packages=find_packages(),
  include_package_data=True,
  install_requires=get_requirements(),
    entry_points="""
        [console_scripts]
        tm=tm.cli:cli
    """,
)