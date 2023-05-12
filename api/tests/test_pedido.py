import requests



ENDPOINT = "http://127.0.0.1:8000/api/pedidos/"
id_ultimo_pedido = 0

class TestPedidoView:
    
    

    #test para crear un pedido con todos los datos requeridos
    def test_post_pedido_datos_completos(self):
        data = {            
            "lista_articulos": [
                {
                "cantidad": "3",
                "referencia": "563"
                }
            ],
            "precio_total_sin_impuestos": "600.00",
            "precio_total_con_impuestos": "7000.00"
        }
        response = requests.post(ENDPOINT, json = data)
        assert response.status_code == 200
        assert response.json() == {'message':  "Pedido creado"}
    
    #test para crear un pedido con articulos no creados
    def test_post_pedido_datos_incorrectos(self):
        data = {            
            "lista_articulos": [
                {
                "cantidad": "3",
                "referencia": "12364"
                },
                {
                "cantidad": "6",
                "referencia": "777"
                }
            ],
            "precio_total_sin_impuestos": "600.00",
            "precio_total_con_impuestos": "7000.00"
        }
        response = requests.post(ENDPOINT, json = data)
        assert response.status_code == 200
        assert response.json()['message'].startswith("No existen los articulos:")
         
    #test para crear un pedido con datos incompletos
    def test_post_pedido_datos_incompletos(self):
        data = {            
            "lista_articulos": [
                {
                "cantidad": "3",
                "referencia": "12364"
                },
                {
                "cantidad": "6",
                "referencia": "777"
                }
            ],
            "precio_total_sin_impuestos": "600.00"
        }
        response = requests.post(ENDPOINT, json = data)
        assert response.status_code == 200
        assert response.json() == {'message' : 'Complete todos los datos necesarios'}

    #test para consultar la lista de todos los pedidos en la BD y seleccionar el id del ultimo
    def test_get_todos_los_pedidos(self):
        global id_ultimo_pedido
        response = requests.get(ENDPOINT)
        assert response.status_code == 200
        id_ultimo_pedido = response.json()['pedidos'][len(response.json()['pedidos'])-1]['id']

    #test para consultar un pedido de BD con un id correcto
    def test_get_pedido_id_correcto(self):
        response = requests.get(ENDPOINT + str(id_ultimo_pedido))
        assert response.status_code == 200
        assert response.json()['pedidos']['id'] == id_ultimo_pedido

    #test para consultar un pedido con un id incorrecto
    def test_get_pedido_id_incorrecto(self):
        response = requests.get(ENDPOINT + str(id_ultimo_pedido+1))
        assert response.status_code == 200
        assert response.json() == {'message':"No se encontro el pedido"}

    #test para actualizar un pedido con un id correcto
    def test_put_pedido_id_correcto(self):
        data = {            
            "lista_articulos": [
                {
                "cantidad": "3",
                "referencia": "563"
                }
            ],
            "precio_total_sin_impuestos": "6700.00",
            "precio_total_con_impuestos": "7000.00" 
        }
        response = requests.put(ENDPOINT + str(id_ultimo_pedido), json = data)
        assert response.status_code == 200
        assert response.json() == {'message':"Pedido actualizado"}
    
    #test para actualizar un pedido con un id incorrecto
    def test_put_pedido_id_incorrecto(self):
        data = {            
            "lista_articulos": [
                {
                "cantidad": "3",
                "referencia": "123"
                }
            ],
            "precio_total_sin_impuestos": "6700.00",
            "precio_total_con_impuestos": "7000.00" 
        }
        response = requests.put(ENDPOINT + str(id_ultimo_pedido+1), json = data)
        assert response.status_code == 200
        assert response.json() == {'message':"No se encontro el pedido"}

    #test para actualizar un pedido con datos faltantes
    def test_put_pedido_datos_incompletos(self):
        data = {            
            "lista_articulos": [
                {
                "cantidad": "3",
                "referencia": "123"
                }
            ],
            "precio_total_sin_impuestos": "6700.00"
        }
        response = requests.put(ENDPOINT + str(id_ultimo_pedido), json = data)
        assert response.status_code == 200
        assert response.json() == {'message':"Complete todos los datos necesarios"}
    
    #test para eliminar un pedido con un id correcto
    def test_delete_pedido_id_correcto(self):
        response = requests.delete(ENDPOINT + str(id_ultimo_pedido))
        assert response.status_code == 200
        assert response.json() == {'message':'Pedido eliminado'}

    #test para eliminar un pedido con un id incorrecto
    def test_delete_pedido_id_incorrecto(self):
        response = requests.delete(ENDPOINT + str(id_ultimo_pedido+1))
        assert response.status_code == 200
        assert response.json() == {'message':'No se encontro el pedido'}