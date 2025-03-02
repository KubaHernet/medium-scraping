from setuptools import setup

requirements_files = [
    '../scraping/requirements.txt',
    'requirements.txt'
]

requirements = []
for file in requirements_files:
    with open(file, 'r', encoding='utf-8') as f:
        requirements += f.read().split('\n')

setup(name='scraping-api',
    version='0.0.1',
    install_requires=requirements,
    py_modules=['api'],
    entry_points={
        'console_scripts': [
            'scrape-api = api:start'
        ]
    }
)
