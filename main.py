from fastapi import FastAPI
from Router.UsuarioRutas import router as usuario_router
from Router.ExamenRutas import router as examen_router
from Router.ReporteRuta import router as reporte_router
from Router.usuarios import router as gemini
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # o ["*"] para permitir todos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Registrar rutas con prefijos por dominio
app.include_router(usuario_router, prefix="/usuario", tags=["Usuario"])
app.include_router(examen_router, prefix="/examen", tags=["Examen"])
app.include_router(reporte_router, prefix="/reporte", tags=["Reporte"])
app.include_router(gemini, prefix="/gemini")
