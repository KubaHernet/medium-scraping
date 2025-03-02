from setuptools import setup, find_packages

with open('../scraping/requirements.txt', 'r', encoding='utf-8') as f:
    requirements = f.read().split('\n')
    
packages=find_packages('../scraping')
    
setup(name='scraping-cli',
    version='0.0.1',
    install_requires=requirements,
    py_modules=['main'],
    packages=packages,
    package_dir={
        'scraping': '../scraping/scraping'
    },
    entry_points={
        'console_scripts': [
            'scrape = main:default'
        ]
    }
)
