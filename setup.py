from setuptools import setup, find_packages

setup(
    name="egyptian-art-analyzer",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "google-generativeai==0.8.5",
        "Pillow==10.4.0",
        "pydantic==2.10.4",
        "python-dotenv==1.0.0",
    ],
    entry_points={
        'console_scripts': [
            'predict=predict:main',
        ],
    },
    python_requires=">=3.11",
)

