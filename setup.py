from setuptools import setup

setup(name='devol',
      version='0.1',
      description='Differential Evolution (DE)',
      url='https://github.com/andaviaco/de',
      author='Andrés Ávila',
      author_email='andaviaco@gmail.com',
      license='MIT',
      packages=['devol'],
      install_requires=[
          'numpy',
      ],
      zip_safe=False)
