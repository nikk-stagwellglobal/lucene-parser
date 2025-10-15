"""Setup configuration for lucene-query-parser package."""

from setuptools import setup, find_packages
from pathlib import Path

setup(
    name="lucene-query-parser",
    version="1.0.0",
    author="Nirmal kumar",
    author_email="nirmal.kumar@stagwellglobal.com",
    description="A Python library for parsing and analyzing Lucene queries",
    long_description=(Path(__file__).parent / "PACKAGE_README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/nikk-stagwellglobal/lucene-parser.git",
    packages=find_packages(exclude=["tests", "lucene-api", "queries", "examples", "attachments"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.13",
    install_requires=["luqum>=1.0.0"],
    keywords="lucene query parser search ast",
    project_urls={
        "Bug Reports": "https://github.com/nikk-stagwellglobal/lucene-parser/issues",
        "Source": "https://github.com/nikk-stagwellglobal/lucene-parser",
    },
)