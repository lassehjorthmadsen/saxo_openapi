from saxo_openapi import API
import saxo_openapi.endpoints.rootservices as rs
from pprint import pprint

with open('C:/Users/LMDN/token24.txt') as f:
    token24 = f.readlines()

token24 = token24[0]

# token = "eyJhbGciOiJFUzI1NiIsIng1dCI6IkRFNDc0QUQ1Q0NGRUFFRTlDRThCRDQ3ODlFRTZDOTEyRjVCM0UzOTQifQ.eyJvYWEiOiI3Nzc3NSIsImlzcyI6Im9hIiwiYWlkIjoiMTA5IiwidWlkIjoibU0zV1o1YU1WTXwyZ201Zk95ckxrdz09IiwiY2lkIjoibU0zV1o1YU1WTXwyZ201Zk95ckxrdz09IiwiaXNhIjoiRmFsc2UiLCJ0aWQiOiIyMDAyIiwic2lkIjoiZWUxZDY3NmU2MmM4NDY0NWFlNzg3ZGYxYzViNjZiOGYiLCJkZ2kiOiI4NCIsImV4cCI6IjE2NzExNzczMzciLCJvYWwiOiIxRiIsImlpZCI6ImU2NjUxMjhjMzNjZTQyNDQzNjgxMDhkYWJkODQ5NjQ1In0.6hnv_sgxP4oLbO0siXZ25NFeAV7DT-0dHAkgvXr7jRgzpiuYdjxJnWNjktxShbHxcvbo_3hHTD-a8WkmsjH-wA"
client = API(access_token=token24)

# lets make a diagnostics request, it should return '' with a state 200
r = rs.diagnostics.Get()
print("request is: ", r)
rv = client.request(r)
assert rv is None and r.status_code == 200
print('diagnostics passed')

# request available rootservices-features
r = rs.features.Availability()
rv = client.request(r)
print("request is: ", r)
print("response: ")
pprint(rv, indent=2)
print(r.status_code)