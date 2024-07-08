import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()


__version__="0.0.0"   

REPO_NAME = "mllflow"
AUTHOR_USER_NAME = "Rishikesh"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "rishikeshram88@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version="__version__",
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="a small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/Riomartin88/mlflow_project.git",
    project_urls={
        "Bug Tracker": f"https://github.com/Riomartin88/mlflow_project.git/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)
