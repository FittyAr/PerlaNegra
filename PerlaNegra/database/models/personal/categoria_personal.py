import reflex as rx
from sqlmodel import Field
from ..mixins.timestamp_mixin import TimestampMixin

class CategoriaPersonal(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    nombre: str