import os,sys
os.system("git pull")
try:
    __import__("POCO").poco()
except Exception as e:
    exit(str(e))
