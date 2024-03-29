try:
    from setuptools import setup, find_packages
except Exception:
    raise ImportError("setuptools is required to install h4cktools!")


setup(
    name="h4cktools",
    version="0.0.3",
    description="h4cktools is a python library containing usefull helpers "
    "for penetration testing and security challenges.",
    url="https://github.com/WhatTheSlime/h4cktools",
    author="Sélim Lanouar",
    author_email="selim.lanouar@gmail.com",
    license="GPLv3",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "urllib3==1.25.9",
        "lxml==4.6.2",
        "requests==2.23.0",
        "beautifulsoup4==4.9.3"
    ],
    extras_require={
        "tests": [
            "pytest==6.1.2",
            "pytest-asyncio==0.14.0",
            "pytest-cov==2.10.1",
            "requests_mock==1.8.0",
        ],
    }
)
