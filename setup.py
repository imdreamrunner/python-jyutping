from distutils.core import setup

setup(
    name='jyutping',
    version='0.3',
    packages=['jyutping',],
    license='MIT',
    author='Ivor Zhou',
    author_email='hello@ivorz.com',
    url='https://github.com/imdreamrunner/python-jyutping',
    description='Python tool to convert Chinese characters to Jyutping.',
    long_description=open('README.rst').read(),
)
