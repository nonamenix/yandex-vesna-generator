from setuptools import setup, find_packages
import os
import vesna

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
]

setup(
    author="Danil Ivanov",
    author_email="nonamenix@gmail.com",
    name='yandex-vesna-generator',
    version=vesna.__version__,
    description='Adds pretty CSS styles for the django CMS admin interface.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    url='http://nonamenix.ru/',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=['lxml', ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)