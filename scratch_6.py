import json

# Data to be written
dictionary = {
    "name": "yuvi",
    "rollno": 55,
    "cgpa": 9.5,
    "phonenumber": "6369980025"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)