from setuptools import setup

setup(
    name="diffnote",
    author="k-xo",
    author_email="alkassimk@gmail.com",
    version="0.3",
    scripts=["diffnote/diffnote.py"],
    url="https://github.com/k-xo/diffnote",
    install_requires=["openai", "tiktoken"],
    entry_points={
        "console_scripts": [
            "diffnote=diffnote:diffnote",
        ],
    },
)
