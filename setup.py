import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='suter',  
     version='0.1',
     scripts=['suther'] ,
     author="Sadi Cesur",
     author_email="cesursadi@gmail.com",
     description="Sutherland's Viscosity Model",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/sadicesur/sutherland",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
