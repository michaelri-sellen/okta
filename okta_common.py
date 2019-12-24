import json

class Common:
    def PrettyPrint(self, rawJson):
        print(json.dumps(json.loads(rawJson), indent=4, sort_keys=True))