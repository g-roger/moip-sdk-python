import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="moip-sdk-python",
    version="0.0.1",
    author="Mastertech",
    description="Integrate Wirecard to your Python application.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mastertech/moip-sdk-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
