from setuptools import setup, find_packages

setup(
    name='biome',
    version='0.1.0',
    author='notrograd',
    description='Biome Build System CLI',
    license='BSD-2-Clause',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
        'gitpython'
    ],
    entry_points={
        'console_scripts': [
            'biome=biome.main:main'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
)

