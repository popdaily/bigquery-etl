from setuptools import setup, find_namespace_packages

def get_version():
    version = {}
    with open('bigquery_etl/_version.py') as fp:
        exec(fp.read(), version)

    return version['__version__']


setup(
    name="format-sql",
    version=get_version(),
    author="Mozilla Corporation",
    author_email="fx-data-dev@mozilla.org",
    description="Tooling for building derived datasets in BigQuery",
    url="https://github.com/mozilla/bigquery-etl",
    packages=find_namespace_packages(include=["bigquery_etl.*", "bigquery_etl"]),
    package_data={'bigquery_etl': ['query_scheduling/templates/*.j2', 'alchemer/*.json']},
    include_package_data=True,
    long_description="Tooling for building derived datasets in BigQuery",
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    entry_points = {
        'console_scripts': ['format-sql=bigquery_etl.format_sql.format:main'],
    },
)
