# xmlextraction using python
Program to extract xml contents from database. This program runs super fast. This program relies on lxml to extract node, node attributes
and associated data. The lxml XML toolkit is a Pythonic binding for the C libraries libxml2 and libxslt. It is unique in that it 
combines the speed and XML feature completeness of these libraries with the simplicity of a native Python AP.  
I have found this to be really fast and based on my benchmarks, I was able to extract data from 1500 files in less than 2 minutes. 
Each of those files were 500 lines. 

# to get this program working
pip install lxml and pip install pyobdc (if you need to connect to database)
