from setuptools import setup, find_packages

setup(
    name='price-tracker',
    version='0.0.1',
    description='Price tracker',
    author='Adam Bogdal',
    author_email='adam@bogdal.pl',
    url='https://github.com/bogdal/price-tracker',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'scrapy==1.0.3',
        'pymongo==3.0.3',
    ],
    entry_points={
        'console_scripts': [
            'run_crawler = price_tracker.crawler:run_crawler']},
)
