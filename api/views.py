from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json
# Create your views here.


class articuloView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id = 0):
        if(id>0):
            articulos = list(articulo.objects.filter(id=id).values())
            if len(articulos) > 0:
                resultado = articulos[0]
                datos={
                    'articulos': resultado
                    }
            else:
                datos={
                    'message':"No se encontro el articulo"
                    }
            return  JsonResponse(datos)
        else:                
            articulos = list(articulo.objects.values())
            if len(articulos)>0:
                datos={
                    'articulos':articulos
                    }
            else:
                datos={
                    'message':"No se encontraros articulos"
                    }
            return  JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        print(jd)
        if (len(jd) == 5):
            articulo.objects.create(
                referencia = jd['referencia'],
                nombre = jd['nombre'],
                descripcion = jd['descripcion'],
                precio_sin_impuestos = jd['precio_sin_impuestos'],
                impuesto_aplicable = jd['impuesto_aplicable']
                )
            datos = {
                'message' : 'Se ha creado un nuevo articulo'
            }
            return JsonResponse(datos)
        
        datos = {
                'message' : 'Complete todos los datos necesarios'
            }
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        if(len(jd) == 5):
            articulos = list(articulo.objects.filter(id=id).values())
            if len(articulos) > 0:
                resultado = articulo.objects.get(id = id)
                resultado.referencia = jd['referencia']
                resultado.nombre = jd['nombre']
                resultado.descripcion = jd['descripcion']
                resultado.precio_sin_impuestos = jd['precio_sin_impuestos']
                resultado.impuesto_aplicable = jd['impuesto_aplicable']
                resultado.save()
                datos={
                        'message':"Articulo actualizado"
                        }
            else:
                datos={
                        'message':'No se encontro el articulo'
                        }
        else:
            datos={
                'message' : 'Complete todos los datos necesarios'
            }
        return  JsonResponse(datos)

    def delete(self, request,id):
        articulos = list(articulo.objects.filter(id=id).values())
        if len(articulos) > 0:
            articulo.objects.filter(id=id).delete()
            datos={
                    'message':"Articulo eliminado"
                    }
        else:
            datos={
                    'message':"No se encontro el articulo"
            }
        return  JsonResponse(datos)


class pedidoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id = 0):
        if(id>0):
            pedidos = list(pedido.objects.filter(id=id).values())
            if len(pedidos) > 0:
                resultado = pedidos[0]
                datos={
                    'pedidos': resultado
                    }
            else:
                datos={
                    'message':"No se encontro el pedido"
                    }
        else:
            pedidos = list(pedido.objects.values())
            if len(pedidos)>0:
                    datos={
                        'pedidos':pedidos
                    }
            else:
                datos={
                    'message':"No se encontraros pedidos"
                    }
        return  JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        if(len(jd)==3):
            articulos_faltantes = []
            for x in jd['lista_articulos']:
                articulos = list(articulo.objects.filter(referencia=x['referencia']).values())
                if (articulos == []):
                    articulos_faltantes.append(x['referencia'] + " ")
            if (articulos_faltantes != []):
                datos = {
                    'message':  "No existen los articulos: "+ "".join(articulos_faltantes)
                }
            else:
                pedido.objects.create(
                    lista_articulos = jd['lista_articulos'],
                    precio_total_sin_impuestos = jd['precio_total_sin_impuestos'],
                    precio_total_con_impuestos = jd['precio_total_con_impuestos'],
                    )
                datos = {
                    'message':  "Pedido creado"
                }
        else:
            datos = {
                'message' : 'Complete todos los datos necesarios'
            }
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        if(len(jd) == 3):
            pedidos = list(pedido.objects.filter(id=id).values())
            if len(pedidos) > 0:
                resultado = pedido.objects.get(id = id)
                articulos_faltantes = []
                for x in jd['lista_articulos']:
                    articulos = list(articulo.objects.filter(referencia=x['referencia']).values())
                    if (articulos == []):
                        articulos_faltantes.append(x['referencia'] + " ")
                print(articulos_faltantes)
                if (articulos_faltantes != []):
                    datos = {
                        'message':  "No se puede actualizar el pedido, no existen los articulos: " + "".join(articulos_faltantes)
                    }
                else:
                    resultado.lista_articulos = jd['lista_articulos']
                    resultado.precio_total_sin_impuestos = jd['precio_total_sin_impuestos']
                    resultado.precio_total_con_impuestos = jd['precio_total_con_impuestos']
                    resultado.save()
                    datos={
                            'message':"Pedido actualizado"
                            }
            else:
                datos={
                        'message':"No se encontro el pedido"
                        }
        else:
            datos={
                'message':"Complete todos los datos necesarios"
            }
        return  JsonResponse(datos)
    
    def delete(self, request,id):
        pedidos = list(pedido.objects.filter(id=id).values())
        if len(pedidos) > 0:
            pedido.objects.filter(id=id).delete()
            datos={
                    'message':"Pedido eliminado"
                    }
        else:
            datos={
                    'message':"No se encontro el pedido"
            }
        return  JsonResponse(datos)