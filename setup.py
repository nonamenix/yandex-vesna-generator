from setuptools import setup, find_packages
import os
import yandex_vesna_generator as vesna

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
    description='Generate crazy Lorem Ipsum text on your site.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    url='https://github.com/nonamenix/yandex-vesna-generator',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=['lxml', 'awesome-slugify'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)