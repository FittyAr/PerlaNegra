import reflex as rx
from sqlmodel import Field
from ..mixins.timestamp_mixin import TimestampMixin

class PruebaHemograma(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    globulos_rojos: int
    hematocritos: int
    hb: int
    vcm: int
    hcm: int
    chcm: int
    rdw: int
    plaquetas: int
    globulos_blancos: int
    formula: str = ''