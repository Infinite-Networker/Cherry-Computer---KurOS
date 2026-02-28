from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cherry-computer-kuros",
    version="1.0.4",
    author="Cherry Computer",
    description="A KurOS-inspired terminal interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Infinite-Networker/Cherry-Computer---KurOS",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "textual>=0.34.0,<9.0.0",
        "rich>=13.0.0",
    ],
    entry_points={
        "console_scripts": [
            "kuros=kuros.app:main",
        ],
    },
)
