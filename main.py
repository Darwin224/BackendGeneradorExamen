from fastapi import FastAPI
from Router.UsuarioRutas import router as usuario_router
from Router.ExamenRutas import router as examen_router
from Router.ReporteRuta import router as reporte_router
from Router.GeminiRuta import router as gemini

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
          # si usas un HTML abierto directo
        "http://localhost:3000",   # tu frontend React
        "http://127.0.0.1:3000"    # opcional, por si usas 127.0.0.1
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





# Registrar rutas con prefijos por dominio
app.include_router(usuario_router, prefix="/usuario", tags=["Usuario"])
app.include_router(examen_router, prefix="/examen", tags=["Examen"])
app.include_router(reporte_router, prefix="/reporte", tags=["Reporte"])
app.include_router(gemini, prefix="/gemini", tags=["Gemini"])
#app.include_router(auth_router, prefix="/auth", tags=["Auth"])
