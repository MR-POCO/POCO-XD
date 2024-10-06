import os,sys
os.system("git pull")
try:
    __import__("OLD").poco()
except Exception as e:
    exit(str(e))
