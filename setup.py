import setuptools
import re

with open("image_knocker/__init__.py", "r") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        f.read(), re.MULTILINE
    ).group(1)

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

def get_requires(filename):
    requirements = []
    with open(filename, "rt") as req_file:
        for line in req_file.read().splitlines():
            if not line.strip().startswith("#"):
                requirements.append(line)
    return requirements

project_requirements = get_requires("./requirements.txt")

setuptools.setup(
    name="image_knocker",
    version=version,
    license='Apache',
    python_requires=">=3.6",
    author="Yonghye Kwon",
    author_email="developer.0hye@gmail.com",
    description="Knock your images before these make you painful",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/developer0hye/image-knocker",
    packages=setuptools.find_packages(),
    install_requires=project_requirements,
    zip_safe=False,
    keywords=['image', 'img'],
    entry_points={
        'console_scripts': ['image-knocker=image_knocker.image_knocker:main']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)