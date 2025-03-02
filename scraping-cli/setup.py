from setuptools import setup

with open('../scraping/requirements.txt', 'r', encoding='utf-8') as f:
    requirements = f.read().split('\n')
    
setup(name='scraping-cli',
    version='0.0.1',
    install_requires=requirements,
    py_modules=['main'],
    entry_points={
        'console_scripts': [
            'scrape = main:default'
        ]
    }
)
