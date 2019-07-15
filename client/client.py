import requests, json

#The caller is able to define which response version (format e.g. JSON and XML ) he can handle.
#By default The caller will receive data in JSON format (only title, content and sender fields)

json_data = requests.get("http://127.0.0.1:5000/message-service")
jd = json.loads(json_data.content)


print("\nData in JSON format ", jd, "\n")


#The same url gives data in xml format (all 4 fields are returned)

xml_data = requests.get("http://127.0.0.1:5000/message-service", headers={"Accept": "application/xml"})
print("Data in XML format ", xml_data.content)