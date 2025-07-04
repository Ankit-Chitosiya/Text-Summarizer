import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

_version_ = "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "Ankit-Chitosiya"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL = "ankitchitosiya00@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=_version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Text Summarizer based on NLP techniques",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ankit-Chitosiya/Text-Summarizer",
    project_urls={
        "Bug Tracker": "https://github.com/Ankit-Chitosiya/Text-Summarizer/issues",
    },
    package_dir = {"": "src"},
    packages=setuptools.find_packages(where="src"),
)




