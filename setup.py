import setuptools

with open('ReadMe.md', 'r') as f:
    long_description = f.read()
    
with open('requirements.txt', 'r', encoding='UTF-16') as f:
    required = f.readlines()


setuptools.setup(
    name="lsystem",
    version="0.0.1",
    
    author="A-Bak",
    author_email="adam.bak.work@gmail.com",
    
    description="Desc.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='',
    url='https://github.com/A-Bak/l-system',
    
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=required,
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)