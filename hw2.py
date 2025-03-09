import json 

pathToFile = "student.json"

updatedFile = "update.json"
    
with open(pathToFile, "r") as file:
    student_str = file.read()


formatted = json.loads(student_str)

formatted["name"] = "Xia Jie"

# with open(updatedFile, "w") as file:    #this just outputs my name 
#     file.write(formatted["name"])


#updating the name and keeping json format
with open(updatedFile, "w") as file:   
    json.dump(formatted, file)