import sys
import os
import time
import pyodbc

from datetime import datetime, date
from lxml import etree
from xml.etree import ElementTree as ET
from io import BytesIO

#Database connection information
sqldbJDBCHostIP=""
sqldbJDBCPort=""
sqldbJDBCHUBLOGDB=""
sqldbDBUserName=""
sqldbPassword=""

#track the extraction time
start = datetime.now();
connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                            "Server=" + sqldbJDBCHostIP + ","+sqldbJDBCPort+";"
                            "Database=" + sqldbJDBCHUBLOGDB + ";"
                            "UID=" + sqldbDBUserName + ";"
                            "PWD=" + sqldbPassword + ";")
cursor = connection.cursor()

SQLCommand = ("Select xmlstring  from TableName")

i=0
files =[];
try:
    cursor.execute(SQLCommand)
    rows = cursor.fetchall()
    for row in rows:
        i= i + 1
        files.append(row.dcxml.encode('utf8'));
except Exception:
       print("no rows exists for xml table")
 

connection.commit()
connection.close()

print("Total xml files: " + str(i));

for w in files:
    some_file_or_file_like_object = BytesIO(w);
    tree = etree.parse(some_file_or_file_like_object)
    root = tree.getroot();
    for element in root.iter():
         print("node:", element.tag);
         print("node value:", element.text);
         hasAttr = len(element.items());
         print("Has Attr", hasAttr);
         for name,value in element.items():
             print("attr:", name);
             print("attr value:",value);
end = datetime.now()
diff = end-start;
print("extraction in minutes : ",+ (diff.total_seconds())/60)
