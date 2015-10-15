# -*- coding: utf-8 -*-
# Copyright (c) 2013-2015, SMARTX

import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='jira-comment-slack',
    version='0.1',
    url='https://github.com/smartxworks/jira-comment-slack',
    license='MIT',
    author='SmartXWorks/Kisung',
    description='Send JIRA comment update to slack channel',
    long_description=__doc__,
    py_modules=["jira_comment_slack"],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'jira-comment-slack-server = jira_comment_slack:main',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
