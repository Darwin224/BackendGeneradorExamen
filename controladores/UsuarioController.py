from db.conexion import supabase
from modelos.UsuarioModel import (
    PersonaCreate, ProfesionCreate, UsuarioFinalCreate,
    EmpleadoCreate, PermisoCreate, UsuarioAdministrativoCreate
)

from db.conexion import supabase
from modelos.UsuarioModel import LoginRequest
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
#-----------------Login----------------#
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


SECRET_KEY = "super_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def crear_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def login_usuario(request: LoginRequest):
    # Traer usuarios con sus relaciones
    response = supabase.schema("usuario").table("usuarioFinal").select("*, profesion(*), persona(*)").execute()
    usuarios = response.data

    # Buscar usuario por correo electrónico en la relación persona
    usuario = next((u for u in usuarios if u["persona"]["correoElectronico"] == request.email), None)
    if not usuario:
        return None, "Usuario no encontrado"

    # Validar contraseña en texto plano
    if request.password != usuario["claveUsuarioFinal"]:
        return None, "Contraseña incorrecta"

    # Crear token JWT
    token = crear_token({"sub": usuario["nombreUsuarioFinal"]})

    return {"token": token, "user": usuario}, None
# ---------- Persona ----------
def crearPersona(persona: PersonaCreate):
    data = persona.model_dump()
    data["fechaDeNacimiento"] = data["fechaDeNacimiento"].isoformat()  # 👈 conversión necesaria
    return supabase.schema("usuario").table("persona").insert(data).execute().data


def obtenerPersonas():
    return supabase.schema("usuario").table("persona").select("*").execute().data

# ---------- Profesion ----------
def crearProfesion(profesion: ProfesionCreate):
    return supabase.schema("usuario").table("profesion").insert(profesion.model_dump()).execute().data

def obtenerProfesiones():
    return supabase.schema("usuario").table("profesion").select("*").execute().data

# ---------- UsuarioFinal ----------
def crearUsuarioFinal(usuario: UsuarioFinalCreate):
    return supabase.schema("usuario").table("usuarioFinal").insert(usuario.model_dump()).execute().data

def obtenerUsuariosFinales():
    return supabase.schema("usuario").table("usuarioFinal").select("*, profesion(*), persona(*)").execute().data

# ---------- Empleado ----------
def crearEmpleado(empleado: EmpleadoCreate):
    return supabase.schema("usuario").table("empleado").insert(empleado.model_dump()).execute().data

def obtenerEmpleados():
    return supabase.schema("usuario").table("empleado").select("*").execute().data

# ---------- Permiso ----------
def crearPermiso(permiso: PermisoCreate):
    return supabase.schema("usuario").table("permiso").insert(permiso.model_dump()).execute().data

def obtenerPermisos():
    return supabase.schema("usuario").table("permiso").select("*").execute().data

# ---------- UsuarioAdministrativo ----------
def crearUsuarioAdministrativo(usuario: UsuarioAdministrativoCreate):
    return supabase.schema("usuario").table("usuarioAdministrativo").insert(usuario.model_dump()).execute().data

def obtenerUsuariosAdministrativos():
    return supabase.schema("usuario").table("usuarioAdministrativo").select("*, empleado(*), permiso(*)").execute().data
