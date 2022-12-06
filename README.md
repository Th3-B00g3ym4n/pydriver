# Pydriver

a useful python library that makes it easier 
to send requests with headers and payloads 

##example

```python
import pydriver

pydriver.data.payload = {'rip' : 'bozo'}
pydriver.data.headers = {}

pydriver.send("https://google.com/")

print(pydriver.response.content)```

##installation

download zip, extract, and put in your 
**/Site-Packages**
