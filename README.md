# Django-API

1. Lo primero que debemos hacer es activar el entorno virtual de python con la siguiente ruta ".\env\Scripts\activate"
2. Creamos el contenedor de docker con el comando "docker-compose build"
3. Iniciamos el contenedor con el comando "docker-compose up"
4. Importar el archivo "Django_API.postman_collection.json" en Postman para cargar la coleccion
5. Para consultar la informacion desde el navegador se debe ingresar a la siguiente ruta "http://localhost:8000/api/articulos/" o "http://localhost:8000/api/pedidos/"
6. Para realizar las pruebas unitarias ingresar el siguiente comando "pytest -v"
