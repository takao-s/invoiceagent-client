import setuptools

install_requires = [
    "requests"
]

packages = [
    'invoiceagent_client',
]

setuptools.setup(
    name='invoiceagent-client',
    version='0.0.1',
    description='Client tool for invoiceAgent Web-API.',
    license='MIT',
    author='takao-s',
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    python_requires=">=3.7",
)
