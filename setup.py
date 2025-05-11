from setuptools import setup, find_packages

setup(
    name="earthguard",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    author="Lyra",
    description="A Python library to enforce Earth-aligned constraints in AI systems",
    long_description=open("README.md").read() if 'README.md' in __import__('os').listdir() else "",
    long_description_content_type="text/markdown",
    url="https://github.com/lyra22/earthguard",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
