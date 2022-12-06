# Pydriver

a useful python library that makes it easier 
to send requests with headers and payloads 

## example

```python
import pydriver

pydriver.data.payload = {'rip' : 'bozo'}
pydriver.data.headers = {}

pydriver.send("https://google.com/")

#prints site content
print(pydriver.response.content)
# prints status
print(pydriver.response.status)
```

## installation

download the zip, extract it, and put in your 
**AppData/Local/Programs/Python/Lib/Site-Packages**
