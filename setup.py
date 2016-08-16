from setuptools import setup

setup(
    name='Mala',
    version='0.1.0',
    description='Get metadata from DHT network',
    long_description=open('README.rst', 'r').read(),
    author='whtsky',
    author_email='whtsky@gmail.com',
    url='https://github.com/whtsky/mala',
    license='BSDv3',
    platforms='any',
    zip_safe=False,
    include_package_data=True,
    py_modules=['mala'],
    install_requires=open("requirements.txt").readlines(),
    keywords=['dht', 'asyncio', 'bt', 'metainfo'],
    classifiers=[
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
