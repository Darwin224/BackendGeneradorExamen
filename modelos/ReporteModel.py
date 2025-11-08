from pydantic import BaseModel
from datetime import date

# ---------- Tablas base ----------

class DatosUsuarioFinal(BaseModel):
    id: int  # antes PKdatosUsuarioFinalID
    edad_promedio: int  # antes edadProemdioDeUsuarioFinal
    cantidad_examen: int  # antes cantidadDeExamen
    cantidad_usuario_final: int  # antes CantidadDeUsuarioFinal

class DatosUsuarioFinalCreate(BaseModel):
    edad_promedio: int
    cantidad_examen: int
    cantidad_usuario_final: int

class Reporte(BaseModel):
    id: int  # antes PKreporteID
    fecha_reporte: date  # antes fechaDeReporte
    usuario_administrativo_id: int  # antes FKusuarioAdministrativoID
    datos_usuario_final_id: int  # antes FKdatoDeUsuarioFinalID

class ReporteCreate(BaseModel):
    fecha_reporte: date
    usuario_administrativo_id: int
    datos_usuario_final_id: int

class DatoDePais(BaseModel):
    id: int | None = None  # ← Supabase puede devolver sin PK explícita
    reporte_id: int  # antes CFKreporteID
    pais: str
    cantidad_por_pais: int  # antes cantidadDeUsuarioFinalPorPais

class DatoDePaisCreate(BaseModel):
    reporte_id: int
    pais: str
    cantidad_por_pais: int

class DatoDeTema(BaseModel):
    id: int | None = None
    reporte_id: int  # antes CFKreporteID
    tema: str
    cantidad_por_tema: int  # antes cantidadPorTema

class DatoDeTemaCreate(BaseModel):
    reporte_id: int
    tema: str
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
