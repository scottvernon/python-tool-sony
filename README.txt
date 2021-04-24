# MD5FILE

A simple webservice to return the md5 hash of an uploaded file.  The file is temporarily written to disk, then removed once the hash has been returned. 
By default the service runs on port 8000 on localhost.  This can be changed by modifying the values in the HOSTNAME & PORT variables within the script.

## Getting Started

Copy md5file.py to the 'server' and run with python3

'''
python3 md5file.py
'''

### Prerequisites

This python script requires an installation of python3.
The client machine requires that curl is installed.


### Usage

On the server start the webservice as described above. Example output below.

'''
$ python3 md5file.py 
Server Started on: localhost 8000
'''

From a client machine use curl to upload a file using XPUT or XPOST and the --upload-file option.

PUT Example

'''
curl -X PUT --upload-file <example.file> http://localhost:8000
'''

POST Example

'''
curl -X POST --upload-file <example.file> http://localhost:8000
'''

Example Client output

'''
curl -X PUT --upload-file awscliv2.zip http://localhost:8000
Hashed "7283b77e9e80e91b1717aa5f4328feeb"
'''

Example Server output

'''
127.0.0.1 - - [03/Dec/2020 09:23:55] "PUT /awscliv2.zip HTTP/1.1" 201 -
'''

### Limitations
This script was written in python3 and does not have built in compatibility with python2 libraries.
There is little exception handling.
There is no support for uploading files from a form.
There is no logging.
