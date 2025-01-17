# database/models/personal.py
import reflex as rx
from sqlmodel import Field
from datetime import date, datetime, timezone
from ..mixins.timestamp_mixin import TimestampMixin


class PersonalR(rx.Model, TimestampMixin, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    apellido: str
    fecha_nacimiento: date
    dni: str
    # numero_legajo: str
    # categoria_personal_id: int = Field(foreign_key='categoriapersonal.id')

    creado_en: datetime = datetime.now(timezone.utc)
    actualizado_en: datetime = datetime.now(timezone.utc)
    estado_civil_id: int = Field(foreign_key="estadocivil.id")
    cantidad_hijos: int = 0
