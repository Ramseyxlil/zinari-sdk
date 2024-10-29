from setuptools import setup, find_packages

setup(
    name="zinaripaysdk",  # Ensure this is your desired package name
    version="0.1.1",      # Change to a new version that hasn't been used
    description="Python SDK for ZinariPay OpenAPI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Abdulrafiu Izuafa",
    author_email="abdulrafiu@techoptimum.org",
    url="https://github.com/Ramseyxlil/zinari-sdk",
    packages=find_packages(),
    install_requires=["requests"],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
