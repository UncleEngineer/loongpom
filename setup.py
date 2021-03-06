from distutils.core import setup
import os.path

def get_file(*paths):
    path = os.path.join(*paths)
    try:
        with open(path, 'rb') as f:
            return f.read().decode('utf8')
    except IOError:
        pass

def get_readme():
    return get_file(os.path.dirname(__file__), 'README.rst')



setup(
  name = 'loongpom',         # How you named your package folder (MyLib)
  packages = ['loongpom'],   # Chose the same as "name"
  version = '0.0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Show Loong Pom Name Jaaa',   # Give a short description about your library
  long_description='plese read in: https://github.com/UncleEngineer/loongpom',
  author = 'Loong Wissawakorn',                   # Type in your name
  author_email = 'loong.wissawakorn2@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/UncleEngineer/loongpom',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/UncleEngineer/loongpom/archive/0.0.1.zip',    # I explain this later on
  keywords = ['LOONGPOM', 'PRAWIT', 'THAILAND', 'UncleEngineer'],   # Keywords that define your package best
  install_requires=[
          'uncleengineer',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
