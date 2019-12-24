import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='FireDetection',  

     version='0.1',

     scripts=['FD'] ,

     author="Rashad Garayev",

     author_email="garayevrashad@hotmail.com",

     description="real time Fire detection",

     long_description=long_description,

   long_description_content_type="text/markdown",

     url="https://github.com/RashadGarayev/FireDetection",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

 )
