# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='django-oidc-auth',
    version='1.0.0',
    description='OpenID Connect client for Django applications',
    long_description='WIP',
    author='Lucas S. Magalhães, Daniel Pimentel, João Paulo de Araújo, Romero Malaquias',
    author_email='lucas.sampaio@intelie.com.br, danielpimentel@lccv.ufal.br, joaopna@lccv.ufal.br, '
                 'romero.malaquias@edge.ufal.br',
    packages=find_packages(exclude=['*.tests']),
    include_package_data=True,
    install_requires=[
        'Django>=3.0,<4.2',
        'South==1.0.2',
        'pyjwkest==1.1.5',
        'requests==2.22.0',
    ],
    zip_safe=True
)
