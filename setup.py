from setuptools import setup, find_packages
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='DeviceControllerTelegramBot',
    author="Dhrumil Mistry",
    version='1.0.0',
    license='MIT License',
    description='A Telegram Bot to control Board Pins for Device Controller Arduino Library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['setuptools',
                      'pyserial',
                      'pyTelegramBotAPI'],
)
