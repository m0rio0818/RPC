import math
import json

class RPC:
    def __init__(self, id, method, params, param_types) -> None:
        self.id = id
        self.method = method
        self.params = params
        self.param_types = param_types
        print(self.params[0], self.params[1], self.method)
    
    def root(self, x):
        return math.floor(x)
     
    def nroot(self, n, x):
        return math.sqrt(x, 1/n)
    
    def reverse(self, s):
        return "".join(list(reversed(s)))
    
    def validAnagram(self):
        return set(self.params[0]) == set(self.params[1])
    
    def sort(self, strArr):
        return sorted(strArr)
    
    def substract(self, x, y):
        print(x, y ," => ",x-y)
        return x - y
    
    def getResult(self):
        result = 0
        type = ""
        if (self.method == "subtract"):
            result = self.substract(int(self.params[0]), int(self.params[1]))
            type = "int"
        elif (self.method == "root"):
            result = self.root(self.params[0])
            type = "int"
        elif(self.method == "nroot"):
            result = self.root(self.params[0], self.params[1])
            type = "int"
        elif (self.method == "reverse"):
            result = self.reverse(self.params[0])
            type = "string"
        elif (self.method == "validAnagram"):
            result = self.validAnagram()
            type = "boolean"
        elif (self.method == "sort"):
            result = self.sort(self.params[0])
            type = "string"
        return [result, type]
    
    
    def makeJson(self):
        result = self.getResult()
        jsonObj = {
            "result" : result[0],
            "result_type" : result[1],
            "id" : self.id
        }
        
        jsonStr = json.dumps(jsonObj)
        return jsonStr
    