import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AutoLabeling",
    version="0.0.1",
    author="rafaelsandroni",
    author_email="rafaelsandronidias@gmail.com",
    description="Few shot learning peudo labeling with gpt3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rafael/gpt3labeling",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "AutoLabeling"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
