#!/usr/bin/env python3

from PIL import Image
from time import sleep
import requests, json
import glob
import argparse
import os
import io


DEEPSTACK_ADDRESS="localhost:5000"

parser = argparse.ArgumentParser(description='Deepstack management tool.')
parser.add_argument('-H','--host', default=DEEPSTACK_ADDRESS, help='Address of deepstack server')
subparser = parser.add_subparsers(dest='action')
r_parser = subparser.add_parser('register')
r_parser.add_argument('name', help='Name to register')


group = r_parser.add_mutually_exclusive_group(required=False)
group.add_argument('-m','--mask', default="*.jpg", help='Mask for files to include e.g. "*.jpg"')
group.add_argument('-p','--path', default=".", help="Path")

d_parser = subparser.add_parser('delete')
d_parser.add_argument('name', help='Name to delete')
l_parser = subparser.add_parser('list')
subparser.default = "list"
args = parser.parse_args()


if args.action == "register":

    if args.path:
       path = args.path + "/" + args.mask
    else:
        path = os.getcwd() + "/" + args.mask

    output = io.BytesIO()
    images = {}
    i = 0
    for file in glob.glob(path):
        img = Image.open(file)
        img.save(output, format='JPEG', quality=100, subsampling=0)
        images["image"+str(i)] = output.getvalue()
        i += 1

    if i > 0:
      response = requests.post("http://"+args.host+"/v1/vision/face/register", files=images, data={"userid":args.name}).json()
      print(response)

elif args.action == "delete":
    response = requests.post("http://"+args.host+"/v1/vision/face/delete", data={"userid":args.name}).json()
    print(response)

elif args.action == "list":
    response = requests.post("http://"+args.host+"/v1/vision/face/list").json()
    print(response)
