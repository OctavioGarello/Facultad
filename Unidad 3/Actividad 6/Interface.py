"""
Defina una interface con los siguientes métodos:

a- insertarElemento: para insertar un objeto en una posición determinada en una colección, teniendo en cuenta el manejo de excepciones cuando la posición donde se vaya a insertar no sea válida.

b- agregarElemento: para agregar un elemento al final de una colección.

c- mostrarElemento: dada una posición de la colección, mostrar los datos del elemento almacenado en dicha posición si esa posición es válida, en caso de que no sea válida lanzar una excepción que controle el error.
"""

from zope.interface import Interface, implementer

class IColeccion(Interface):  # type: ignore
	def insertarElemento(self, posicion, elemento):
		pass
	def agregarElemento(self, elemento):
		pass
	def mostrarElemento(self, posicion):
		pass
	def mostrarElementoLista(self, posicion):
		pass
	def mostrarCantidadLista(self):
		pass
	def mostrarMarcaLavarropas(self):
		pass
	def mostrarLista(self):
		pass
	def GuardarJson(self,ruta):
		pass