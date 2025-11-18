from pydantic import BaseModel
from datetime import date

# ---------- Tablas base ----------

class DatosUsuarioFinal(BaseModel):
    PKdatosDeUsuarioFinalID: int  # antes PKdatosUsuarioFinalID
    edadPromedioDeUsuarioFinal: int  # antes edadProemdioDeUsuarioFinal
    cantidadDeExamen: int  # antes cantidadDeExamen
    cantidadDeUsuarioFinal: int  # antes CantidadDeUsuarioFinal
    FKdatoDeUsuarioFinal: int  # antes FKdatoDeUsuarioFinalID

class DatosUsuarioFinalCreate(BaseModel):
    edadPromedioDeUsuarioFinal: int  # antes edadProemdioDeUsuarioFinal
    cantidadDeExamen: int  # antes cantidadDeExamen
    cantidadDeUsuarioFinal: int  # antes CantidadDeUsuarioFinal
    FKdatoDeUsuarioFinal: int  # antes FKdatoDeUsuarioFinalID

class Reporte(BaseModel):
    PKreporteID: int  # antes PKreporteID
    fechaDeReporte: date  # antes fechaDeReporte
    FKusuarioAdministrativoID: int  # antes FKusuarioAdministrativoID

class ReporteCreate(BaseModel):
    fechaDeReporte: date  # antes fechaDeReporte
    FKusuarioAdministrativoID: int  # antes FKusuarioAdministrativoID

class DatoDePais(BaseModel):
    CFKreporteID: int  # antes CFKreporteID
    pais: str
    cantidadDeUsuarioFinalPorPais: int  # antes cantidadDeUsuarioFinalPorPais

class DatoDePaisCreate(BaseModel):
    CFKreporteID: int  # antes CFKreporteID
    cantidadDeUsuarioFinalPorPais: int  # antes cantidadDeUsuarioFinalPorPais


class DatoDeTema(BaseModel):
    CFKreporteID: int  # antes CFKreporteID
    tema: str
    cantidadPorTema: int  # antes cantidadPorTema

class DatoDeTemaCreate(BaseModel):
    reporte_id: int
    cantidad_por_tema: int

# ---------- Modelos para solicitudes GET con joins ----------

# ✅ Para GET con join: reporte + datosUsuarioFinal
class ReporteRead(BaseModel):
    id: int
    fecha_reporte: date
    usuario_administrativo_id: int
    datos_usuario_final: DatosUsuarioFinal  # ← join con DatosUsuarioFinal

# ✅ Para GET con join: datoDePais + reporte
class DatoDePaisRead(BaseModel):
    id: int | None = None
    pais: str
    cantidad_por_pais: int
    reporte: Reporte  # ← join con Reporte

# ✅ Para GET con join: datoDeTema + reporte
class DatoDeTemaRead(BaseModel):
    id: int | None = None
    tema: str
    cantidad_por_tema: int
    reporte: Reporte  # ← join con Reporte
