from setuptools import setup, find_packages
import pathlib


here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")


setup(
    name="open-bobj",
    version="0.1.1",
    description=("Open obj files in Blender from Terminal"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PraxTube/open-bobj",
    author="Prax",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="blender, obj",
    package_dir={"": "src"},
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(where="src"),
    include_package_data=True,
    python_requires=">=3.8, <4",
    install_requires=[],
    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    # extras_require={
    #    "dev": ["check-manifest"],
    #    "test": ["coverage"],
    # },
    # Entry points. The following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    entry_points={
        "console_scripts": [
            "bobj=open_bobj:main.main",
            "open-bobj=open_bobj:main.main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/PraxTube/open-bobj/issues",
        "Source": "https://github.com/PraxTube/open-bobj",
    },
)
