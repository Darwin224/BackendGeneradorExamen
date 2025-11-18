from fastapi import APIRouter, HTTPException
from modelos.UsuarioModel import (
    LoginRequest, PersonaCreate, ProfesionCreate, UsuarioFinalCreate,
    EmpleadoCreate, PermisoCreate, UsuarioAdministrativoCreate
)
from controladores.UsuarioController import (
    crearPersona, login_usuario, obtenerPersonas,
    crearProfesion, obtenerProfesiones,
    crearUsuarioFinal, obtenerUsuariosFinales,
    crearEmpleado, obtenerEmpleados,
    crearPermiso, obtenerPermisos,
    crearUsuarioAdministrativo, obtenerUsuariosAdministrativos
)

router = APIRouter()

#-------------Login-----------#
@router.post("/login")
def ruta_login(request: LoginRequest):
    result, error = login_usuario(request)
    if error:
        raise HTTPException(status_code=401, detail=error)
    return result

# ---------- Persona ----------
@router.post("/crearPersona")
def ruta_crear_persona(persona: PersonaCreate):
    return crearPersona(persona)

@router.get("/obtenerPersonas")
def ruta_obtener_personas():
    return obtenerPersonas()

# ---------- Profesion ----------
@router.post("/crearProfesion")
def ruta_crear_profesion(profesion: ProfesionCreate):
    return crearProfesion(profesion)

@router.get("/obtenerProfesiones")
def ruta_obtener_profesiones():
    return obtenerProfesiones()

# ---------- UsuarioFinal ----------
@router.post("/crearUsuarioFinal")
def ruta_crear_usuario_final(usuario: UsuarioFinalCreate):
    return crearUsuarioFinal(usuario)

@router.get("/obtenerUsuariosFinales")
def ruta_obtener_usuarios_finales():
    return obtenerUsuariosFinales()

# ---------- Empleado ----------
@router.post("/crearEmpleado")
def ruta_crear_empleado(empleado: EmpleadoCreate):
    return crearEmpleado(empleado)

@router.get("/obtenerEmpleados")
def ruta_obtener_empleados():
    return obtenerEmpleados()

# ---------- Permiso ----------
@router.post("/crearPermiso")
def ruta_crear_permiso(permiso: PermisoCreate):
    return crearPermiso(permiso)

@router.get("/obtenerPermisos")
def ruta_obtener_permisos():
    return obtenerPermisos()

# ---------- UsuarioAdministrativo ----------
@router.post("/crearUsuarioAdministrativo")
def ruta_crear_usuario_administrativo(usuario: UsuarioAdministrativoCreate):
    return crearUsuarioAdministrativo(usuario)

@router.get("/obtenerUsuariosAdministrativos")
def ruta_obtener_usuarios_administrativos():
    return obtenerUsuariosAdministrativos()
