import requests
import json

if __name__ == '__main__':
    url = 'https://httpbin.org/put'
    payload = { 'nombre': 'Arturo', 'curso': 'python', 'nivel': 'intermedio'}
    headers = { 'Content-Type': 'application/json', 'acces-token': '12334234'}

    response = requests.put(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_json = json.loads(response.text)
        headers_response = response.headers #Diccionario
        print(headers_response)

        server = headers_response['Server']
        print(server)        

        content = response.content
        file = open('return.json', 'wb')
        file.write(content)
        file.close()
        