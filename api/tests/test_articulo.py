import requests

ENDPOINT = "http://127.0.0.1:8000/api/articulos/"
id_ultimo_articulo = 0

class TestArticuloView:

    #test para crear un articulo con todos los datos requeridos
    def test_post_articulo_datos_completos(self):
        data = {
            "referencia": "563",
            "nombre": "Waffer",
            "descripcion": "galletas waffer",
            "precio_sin_impuestos": "500.00",
            "impuesto_aplicable": 15
        }
        response = requests.post(ENDPOINT, json = data)
        assert response.status_code == 200
        assert response.json() == {'message' : 'Se ha creado un nuevo articulo'}
    
    #test para crear un articulo sin todos los datos requeridos
    def test_post_articulo_datos_incompletos(self):
        data = {
            "referencia": "563",
            "nombre": "Waffer",
            "descripcion": "galletas waffer",
            "precio_sin_impuestos": "500.00"
        }
        response = requests.post(ENDPOINT, json = data)
        assert response.status_code == 200 
        assert response.json() == {'message' : 'Complete todos los datos necesarios'}

    #test para consultar la lista de todos los articulos en la BD y seleccionar el id del ultimo
    def test_get_todos_los_articulos(self):
        global id_ultimo_articulo
        response = requests.get(ENDPOINT)
        assert response.status_code == 200
        id_ultimo_articulo = response.json()['articulos'][len(response.json()['articulos'])-1]['id']

    #test para consultar un articulo de la BD con un id correcto
    def test_get_articulo_id_correcto(self):
        response = requests.get(ENDPOINT + str(id_ultimo_articulo))
        assert response.status_code == 200
        assert response.json()["articulos"]["id"] == id_ultimo_articulo
       
    #test para consultar un articulo con un id incorrecto
    def test_get_articulo_id_incorrecto(self):
        response = requests.get(ENDPOINT + str(id_ultimo_articulo+1))
        assert response.status_code == 200
        assert response.json() == {'message':"No se encontro el articulo"}

    #test para actualizar un articulo con un id correcto
    def test_put_articulo_id_correcto(self):
        data = {
            "referencia": "456",
            "nombre": "Ducales",
            "descripcion": "galletas ducales",
            "precio_sin_impuestos": "5000.00",
            "impuesto_aplicable": 15
        }
        response = requests.put(ENDPOINT + str(id_ultimo_articulo), json = data)
        assert response.status_code == 200
        assert response.json() == {'message':"Articulo actualizado"}

    #test para actualizar un articulo con un id incorrecto
    def test_put_articulo_id_incorrecto(self):
        data = {
            "referencia": "777",
            "nombre": "Hit",
            "descripcion": "Jugo Hit",
            "precio_sin_impuestos": "2500.00",
            "impuesto_aplicable": 15
        }
        response = requests.put(ENDPOINT + str(id_ultimo_articulo+1), json = data)
        assert response.status_code == 200
        assert response.json() == {'message':'No se encontro el articulo'}
    
    #test para actualizar un articulo con datos faltantes
    def test_put_articulo_datos_incompletos(self):
        data = {
            "referencia": "777",
            "nombre": "Hit",
            "descripcion": "Jugo Hit",
            "precio_sin_impuestos": "2500.00"
        }
        response = requests.put(ENDPOINT + str(id_ultimo_articulo), json = data)
        assert response.status_code == 200
        assert response.json() == {'message' : 'Complete todos los datos necesarios'}

    #test para eliminar un articulo con un id correcto
    def test_delete_articulo_id_correcto(self):
        response = requests.delete(ENDPOINT + str(id_ultimo_articulo))
        assert response.status_code == 200
        assert response.json() == {'message':"Articulo eliminado"}

    #test para eliminar un articulo con un id incorrecto
    def test_delete_articulo_id_incorrecto(self):
        response = requests.delete(ENDPOINT + str(id_ultimo_articulo+1))
        assert response.status_code == 200
        assert response.json() == {'message':"No se encontro el articulo"}


#Se crea un nuevo articulo para agregarlo en los pedidos
articulo = TestArticuloView()
articulo.test_post_articulo_datos_completos()