from setuptools import setup, find_packages

setup(
    name="cryptodown",
    version="1.0.0",
    description="Offline CNS Lab Program Generator for Lab Exams",
    long_description=open("README.md", encoding="utf-8").read() if __import__("os").path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "cryptodown=cnslab.cli:main",
            "cnslab=cnslab.cli:main",
            "cns=cnslab.cli:main",
        ],
    },
)
