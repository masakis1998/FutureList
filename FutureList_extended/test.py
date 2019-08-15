import sys
import json

data = {"username": sys.argv[1], "rounds": sys.argv[2]}

with open("inputs.json", "w") as jsonFile:
    json.dump(data, jsonFile)

print(sys.argv[1])
