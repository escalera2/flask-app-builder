from datetime import datetime
from flask_appbuilder.security.sqla.models import User
from . import db


class Categoria(db.Model):
    __tablename__ = "categorias"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    descripcion = db.Column(db.String(250), nullable=True)
    activo = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return self.nombre


class Ingrediente(db.Model):
    __tablename__ = "ingredientes"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey(
        "categorias.id"), nullable=False)
    cantidad = db.Column(db.Numeric(12, 3), nullable=False)
    unidad_medida = db.Column(db.String(20), nullable=False)
    costo_unitario = db.Column(db.Numeric(12, 2), nullable=False)
    stock_minimo = db.Column(db.Numeric(12, 3), nullable=False)
    fecha_vencimiento = db.Column(db.Date, nullable=True)
    activo = db.Column(db.Boolean, default=True)

    categoria = db.relationship(
        "Categoria", backref=db.backref("ingredientes", lazy=True))

    def __repr__(self):
        return self.nombre


class Plato(db.Model):
    __tablename__ = "platos"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    precio = db.Column(db.Numeric(12, 2), nullable=False)
    activo = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return self.nombre


class Receta(db.Model):
    __tablename__ = "recetas"
    id = db.Column(db.Integer, primary_key=True)
    plato_id = db.Column(db.Integer, db.ForeignKey(
        "platos.id"), nullable=False)
    ingrediente_id = db.Column(db.Integer, db.ForeignKey(
        "ingredientes.id"), nullable=False)
    cantidad_necesaria = db.Column(db.Numeric(12, 3), nullable=False)

    plato = db.relationship("Plato", backref=db.backref("recetas", lazy=True))
    ingrediente = db.relationship(
        "Ingrediente", backref=db.backref("recetas", lazy=True))


class MovimientoInventario(db.Model):
    __tablename__ = "movimientos_inventario"
    id = db.Column(db.Integer, primary_key=True)
    ingrediente_id = db.Column(db.Integer, db.ForeignKey(
        "ingredientes.id"), nullable=False)

    usuario_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    tipo = db.Column(db.String(10), nullable=False)
    cantidad = db.Column(db.Numeric(12, 3), nullable=False)
    motivo = db.Column(db.String(250), nullable=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    ingrediente = db.relationship(
        "Ingrediente", backref=db.backref("movimientos", lazy=True))
    usuario = db.relationship(
        User, backref=db.backref("movimientos", lazy=True))
