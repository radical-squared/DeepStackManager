# deepstack manager

Simple command-line tool to manage faces "memory" of deepstack instance. It provides simple means to register, delete and list faces as well as submit images for face recognition or object detection. 

The script simplifies registering face with multiple images by submitting all image files present in current directory.  

<pre>

$ dsm -h
usage: dsm [-h] [-H HOST] {register,recognize,detect,delete,list} ...

Deepstack management tool.

positional arguments:
  {register,recognize,detect,delete,list}

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



$ dsm recognize -h
usage: dsm recognize [-h] file

positional arguments:
  file        File to submit for face recognition



$ dsm detect -h
usage: dsm detect [-h] file

positional arguments:
  file        File to submit for object detection



$ dsm delete -h
usage: dsm delete [-h] name

positional arguments:
  name        Name to delete
