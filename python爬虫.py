import json

fp = open("E:/vscode_code/python code/python-Reptile/test.txt","r")

content = json.load(fp)

print(type(content))

fp.close()
