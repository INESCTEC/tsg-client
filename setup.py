from setuptools import setup
from pip._internal.req import parse_requirements


def load_requirements(file_name):
    try:
        return [str(req.req) for req in parse_requirements(file_name, session=False)]
    except AttributeError:
        return [str(req.requirement) for req in parse_requirements(file_name, session=False)]


setup(
    name='tsg-client',
    version='0.0.1',
    packages=['tsg_client', 'tsg_client.controllers', 'tsg_client.utils'],
    url='',
    license='',
    author='Carolina Catorze, Vasco Maia, José Luis Rodrigues, José Ricardo Andrade',
    author_email="""
        - carolina.catorze@inesctec.pt
        - vasco.r.maia@inesctec.pt
        - jose.l.rodrigues@inesctec.pt
        - jose.r.andrade@inesctec.pt
    """,
    description='TSG Client is a Python library for interacting with the TNO Security Gateway (TSG). It '
                'provides a simple and easy-to-use interface for tasks such as: Connecting to TSG connectors, '
                'Retrieving connector self-descriptions, Working with catalogs and artifacts, Requesting and '
                'consuming data artifacts, Knowing what connectors are in the dataspace, Take advantage of the '
                'OpenAPI functionalities',
    install_requires=load_requirements("requirements.in")
)
