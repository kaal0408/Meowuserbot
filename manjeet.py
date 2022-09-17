import os
import zipfile
from base64 import b64decode
SOURCE_CODE = "aHR0cHM6Ly9naXRodWIuY29tL2thYWwwNDA4L01lb3dVc2VyYm90L2FyY2hpdmUvbWFpbi56aXA="

def xyz():
    os.mkdir("ayo")
    code = SOURCE_CODE.encode()
    url = b64decode(code).decode("utf-8")
    branch = os.environ.get("BRANCH", "main")
    os.system(f"git clone -b {branch} {url} ayo")
    from time import sleep
    sleep(3.5)
    print("!!! Cloned Source Code !!!")

xyz()
 
os.system("bash start")
