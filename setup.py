from setuptools import setup, find_packages
setup(
    name='azurepyscripts',
    version='1.0',
    author='Alexis Ibarra',
    description='some auto scripts deployments',
    url='https://github.com/axisSN01/Azure-AZ-900-Scripts',
    keywords='development, setup, setuptools',
    python_requires='>=3.9',
    install_requires=[
        'azure-mgmt-resource',
        'azure-mgmt-compute',
        'azure-mgmt-network',
        'azure-identity',
        'msal',
        'msrestazure',  
    ],
    packages=find_packages(),
)
