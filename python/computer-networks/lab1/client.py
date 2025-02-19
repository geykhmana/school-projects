import http.client
import sys

host = sys.argv[1]
port = int(sys.argv[2])
filename = sys.argv[3]

connection = http.client.HTTPSConnection(host, port)
connection.request("GET", filename)
response = connection.getresponse()

print(f"Status: {response.status}, Reason: {response.reason}")
print(response.read().decode)

connection.close