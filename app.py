import os
from flask import Flask, jsonify, request
import copy
  
app = Flask(__name__)

    
person1 = {
  "id": 1,
  "name": "Edith",
  "lastname": "Johnson",
  "relationship": "grandmother",
  "age": 77
}
person2 = {
  "id": 2,
  "name": "Jeffrey",
  "lastname": "Johnson",
  "relationship": "grandfather",
  "age": 79
}
person3 = {
  "id": 3,
  "name": "Grace",
  "lastname": "Jones",
  "relationship": "grandmother",
  "age": 65
}
person4 = {
  "id": 4,
  "name": "Frederick",
  "lastname": "Jones",
  "relationship": "grandfather",
  "age": 70
}
person5 = {
  "id": 5,
  "name": "Carol",
  "lastname": "Johnson",
  "relationship": "mother",
  "age": 47
  
}
person6 = {
  "id": 6,
  "name": "Jonathan",
  "lastname": "Johnson",
  "relationship": "father",
  "age": 44
}
person7 = {
  "id": 7,
  "name": "Zachary",
  "lastname": "Johnson",
  "relationship": "child", 
  "age": 17
}

family = {
  "relationship" : "",
  "members": [person1, person2, person3, person4, person5, person6, person7]
}

@app.route('/', methods=['GET'])
def ageism():
  
  fam = copy.deepcopy(family["members"])
  fam.sort(key=lambda x:x['age'], reverse=True)
  response2 = jsonify({"status code":200, "data":fam})
  return response2
  


app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))