from setuptools import setup, find_packages

setup(
    name="gisflask",
    version="0.1.4",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask>=2.0.0',
        'Flask-SQLAlchemy>=3.0.0',
        'Flask-Login>=0.6.0',
        'Flask-WTF>=1.0.0',
        'SQLAlchemy>=2.0.0',
        'Werkzeug>=2.0.0',
        'email-validator>=1.0.0',
        'python-dotenv>=0.19.0',
        'folium>=0.12.0',
        'geopandas>=0.10.0',
        'shapely>=1.8.0',
        'geopy>=2.2.0',
        'pandas>=1.3.0',
        'numpy>=1.21.0',
        'requests>=2.26.0',
        'gunicorn>=20.1.0',
        'psycopg2-binary>=2.9.0',
        'alembic>=1.7.0',
        'pytest>=6.2.0',
        'pytest-cov>=2.12.0',
        'black>=21.5b2',
        'flake8>=3.9.0',
        'mypy>=0.910',
        'isort>=5.9.0',
        'pre-commit>=2.15.0',
        'sphinx>=4.0.0',
        'sphinx-rtd-theme>=0.5.0',
        'twine>=3.4.0',
        'wheel>=0.37.0',
        'build>=0.7.0'
    ],
    extras_require={
        'dev': [
            'pytest>=6.2.0',
            'pytest-cov>=2.12.0',
            'black>=21.5b2',
            'flake8>=3.9.0',
            'mypy>=0.910',
            'isort>=5.9.0',
            'pre-commit>=2.15.0',
            'sphinx>=4.0.0',
            'sphinx-rtd-theme>=0.5.0',
            'twine>=3.4.0',
            'wheel>=0.37.0',
            'build>=0.7.0'
        ]
    },
    python_requires='>=3.9',
    author="Lawrence Kimutai",
    author_email="lawrencekimutai001@gmail.com",
    description="A Flask-based GIS backend package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KimutaiLawrence/gisflask",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering :: GIS',
        'Framework :: Flask',
    ],
    entry_points={
        'console_scripts': [
            'gisflask=gisflask.cli:main',
        ],
    },
)