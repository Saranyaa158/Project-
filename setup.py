from setuptools import setup
with  open("README.md","r",encoding="utf-8") as f:
    long_description =f.read()





    REPO_NAME="project"
    AUTHOR_USER_NAME = "Saranyaa158"
    SRC_REPO = "src"
    LIST_OF_REQUIREMENTS = ['streamlit','numpy']


    setup(
        name=SRC_REPO,
        version="0.0.1",
        author=AUTHOR_USER_NAME,
        description="A small package for book recommendation system",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
        author_email="23mca024@stc.ac.in",
        packages=[SRC_REPO],
        python_requires=">=3.7",
        install_requirements=LIST_OF_REQUIREMENTS
 )