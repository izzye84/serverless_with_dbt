from setuptools import find_packages, setup

setup(
    name="quickstart_etl",
    packages=find_packages(exclude=["quickstart_etl_tests"]),
    package_data={
        "my-dagster-code-location": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster",
        "dagster-dbt",
        "dagster-cloud",
        "boto3",
        "pandas",
        "matplotlib",
        "textblob",
        "tweepy",
        "wordcloud",
        "dagster-dbt",
        "dbt-duckdb<1.9",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
