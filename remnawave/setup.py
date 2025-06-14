from setuptools import setup, find_packages

setup(
    name="remnawave",
    version="0.1.0",
    description="Async Python client for Remnawave panel API",
    author="Tim-oxa",
    author_email="tim@otso.city",
    packages=find_packages(),
    install_requires=[
        "httpx"
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
