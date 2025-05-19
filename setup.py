from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gisflask",
    version="0.1.0",
    author="GIS Flask Team",
    author_email="example@example.com",
    description="A Flask-based GIS backend package with JWT authentication, role-based permissions, interactive maps, and API documentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/gisflask",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Flask",
        "Topic :: Scientific/Engineering :: GIS",
    ],
    python_requires=">=3.7",
    install_requires=[
        "flasgger>=0.9.7",
        "Flask>=2.3.3",
        "Flask-Bcrypt>=1.0.1",
        "Flask-Cors>=4.0.0",
        "Flask-JWT-Extended>=4.5.3",
        "Flask-Migrate>=4.0.5",
        "Flask-SQLAlchemy>=3.1.1",
        "folium>=0.14.0",
        "gunicorn>=21.2.0",
        "marshmallow>=3.20.1",
        "psycopg2-binary>=2.9.9",
        "SQLAlchemy>=2.0.23",
        "Werkzeug>=2.3.7",
        "email-validator>=2.1.0",
    ],
    entry_points={
        "console_scripts": [
            "gisflask=app.cli:main",
        ],
    },
)