from setuptools import setup

setup(
    name='consul-lock',
    version='0.1.8',
    description='Distributed locking built on top of Consul.',
    url='http://github.com/oysterbooks/python-consul-lock',
    author='Oyster',
    author_email='engineering@oysterbooks.com',
    license='MIT',
    packages=['consul_lock'],
    tests_require=['mock'],
    install_requires=['python-consul'],
    zip_safe=True
)
