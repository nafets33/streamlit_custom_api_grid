from setuptools import setup, find_packages
# Try to read README, but don't fail if it doesn't exist
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "A Streamlit Aggrid custom component with Custom Button Modal and API integration"

setup(
    name="streamlit-custom_api_grid",
    version="0.1.4",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.0.0",
    ],
    include_package_data=True,  # Ensure package data is included
    package_data={
        "streamlit_custom_api_grid": ["frontend/build/**/*"],  # Include all files in build
    },
    author="Stefan Stapinski",
    author_email="stefanstapinski@gmail.com",  # Use your actual TestPyPI email
    description="A Streamlit Aggrid custom component with Custom Button Modal and API integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nafets33/streamlit_custom_api_grid",
    project_urls={
        "Bug Tracker": "https://github.com/nafets33/streamlit_custom_api_grid/issues",
    },
    python_requires=">=3.7",
)

# rm -rf dist/ build/ *.egg-info

# python setup.py sdist bdist_wheel

# twine upload dist/*