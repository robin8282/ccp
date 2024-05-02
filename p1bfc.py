import requests
import xml.etree.ElementTree as ET  

url = "https://www.w3schools.com/xml/tempconvert.asmx"

SOAPEnvelope = """<?xml version="1.0" encoding ="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <FahrenheitToCelsius xmlns="https://www.w3schools.com/xml/">
      <Fahrenheit>102.2</Fahrenheit>
    </FahrenheitToCelsius>
  </soap:Body>
</soap:Envelope>"""

headers = {
    "Content-Type": "text/xml; charset=utf-8",
    "SOAPAction": "https://www.w3schools.com/xml/FahrenheitToCelsius"   
}

response = requests.post(url, data=SOAPEnvelope, headers=headers)
root =ET.fromstring(response.text)

for child in root.iter("{https://www.w3schools.com/xml/}FahrenheitToCelsiusResult"):
    C2F=child.text
    print(C2F)
