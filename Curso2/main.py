import requests
import json

if __name__ == '__main__':
    url = 'https://i.blogs.es/23b58b/star-wars-wallpapers-6/1366_2000.jpg'

    response = requests.get(url, stream=True) #Realizar una peticion sin descargar el contenido 
    with open('image.jpg', 'wb') as file:
        for chunk in response.iter_content(): #Descarga el contenido poco a poco
            file.write(chunk)

    response.close() 