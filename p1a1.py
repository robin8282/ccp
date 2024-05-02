from zeep import Client
client = Client('http://localhost:10000/?wsdl')
result = client.service.add_numbers(5, 10)
print(f"Result from the SOAP service:{result}")
