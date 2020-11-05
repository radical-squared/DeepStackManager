# dsm
deepstack manager
<pre>
Simple python script to list, register or delete faces in deepstack instance. Allows registering multiple images at a time. 


$ dsm -h
usage: dsm [-h] [-H HOST] {register,delete,list} ...

Deepstack management tool.

positional arguments:
  {register,delete,list}

optional arguments:
  -h, --help            show this help message and exit
  -H HOST, --host HOST  Address of deepstack server


$ dsm register -h
usage: dsm register [-h] [-m MASK | -p PATH] name

positional arguments:
  name                  Name to register

optional arguments:
  -h, --help            show this help message and exit
  -m MASK, --mask MASK  Mask for files to include
  -p PATH, --path PATH  Path


$ dsm delete -h
usage: dsm delete [-h] name

positional arguments:
  name        Name to delete

optional arguments:
  -h, --help  show this help message and exit
