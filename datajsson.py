import json
import yaml
with open ('myfile.json', 'r') as json_file:
   ourjson = json.load (json_file)
print (ourjson)
print ("\n El token de acceso es :{}".format(ourjson['access_token']))
print ("\n El token expira en :{}".format(ourjson['expires_in']))