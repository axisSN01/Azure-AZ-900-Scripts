from setuptools import setup
setup(
    name='azure_scripts'
    version='1.0',
    author='Alexis Ibarra',
    description='some auto scripts deployments',
    url='https://github.com/axisSN01/Azure-AZ-900-Scripts',
    keywords='development, setup, setuptools',
    python_requires='>=3.11',
    install_requires=[
        'azure-mgmt-resource',
        'azure-mgmt-compute',
        'azure-mgmt-network',
        'azure-identity',
    ],
    }
)
