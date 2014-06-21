from setuptools import setup


setup(
    name='django-behave',
    packages=['django_behave'],
    version='0.1.2',
    description='Django Test Runner for the Behave BDD module',
    author='Rachel Willmer',
    author_email='rachel@willmer.org',
    url='https://github.com/rpaloschi/django-behave',
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Testing',
    ],
    install_requires=[
        'Django>=1.6',
        'selenium',
        'parse',
        'behave',
    ]
)
