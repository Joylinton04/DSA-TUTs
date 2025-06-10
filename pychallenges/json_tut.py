import json


person = {
    "name": "Joylinton",
    "age": 17,
    "id": 1,
}

json_string = json.dumps(person)
original_person = json.loads(json_string)

print(type(original_person))