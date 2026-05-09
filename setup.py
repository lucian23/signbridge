from setuptools import setup, find_packages

setup(
    name='signbridge',
    version='1.0.0',
    description='Simulator LSR — Invata limbajul semnelor romanesc, InfoEducatie 2026',
    packages=find_packages(),
    install_requires=['ttkbootstrap>=1.10', 'Pillow>=10.0'],
    python_requires='>=3.11',
    entry_points={'console_scripts': ['signbridge=signbridge.main:main']},
)
