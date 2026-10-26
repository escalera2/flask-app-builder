from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from . import appbuilder
from .models import Categoria, Ingrediente, Plato, Receta, MovimientoInventario


class CategoriaModelView(ModelView):
    datamodel = SQLAInterface(Categoria)
    list_columns = ["nombre", "descripcion", "activo"]


class IngredienteModelView(ModelView):
    datamodel = SQLAInterface(Ingrediente)
    list_columns = ["nombre", "categoria", "cantidad",
                    "unidad_medida", "costo_unitario", "stock_minimo", "activo"]


class PlatoModelView(ModelView):
    datamodel = SQLAInterface(Plato)
    list_columns = ["nombre", "precio", "activo"]


class RecetaModelView(ModelView):
    datamodel = SQLAInterface(Receta)
    list_columns = ["plato", "ingrediente", "cantidad_necesaria"]


class MovimientoInventarioModelView(ModelView):
    datamodel = SQLAInterface(MovimientoInventario)
    list_columns = ["fecha", "ingrediente",
                    "tipo", "cantidad", "usuario", "motivo"]


appbuilder.add_view(CategoriaModelView, "Categorías", icon="fa-folder",
                    category="Inventario", category_icon="fa-archive")
appbuilder.add_view(IngredienteModelView, "Ingredientes",
                    icon="fa-apple", category="Inventario")
appbuilder.add_view(PlatoModelView, "Platos", icon="fa-cutlery",
                    category="Cocina", category_icon="fa-book")
appbuilder.add_view(RecetaModelView, "Recetas",
                    icon="fa-list-alt", category="Cocina")
appbuilder.add_view(MovimientoInventarioModelView,
                    "Movimientos", icon="fa-exchange", category="Inventario")
