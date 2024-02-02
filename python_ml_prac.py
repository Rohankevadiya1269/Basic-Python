import sys # Here we are importing sys module to know the python version 
print("python version")
print(sys.version)          # It will return 3.10 as the version of the python in this system is 3.10
print(sys.version_info)


# Now we will test date and time method of python
import datetime
now = datetime.datetime.now()
print(now)