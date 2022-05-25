from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    return 'Estimaciones home'


@app.route('/estimaciones', methods=['GET'])
def get_estimaciones():
    
    estimaciones = {
      "Estimaciones": [
        {
          "id_proyecto": "py_1",
          "datos": [
            {
              "id": "1",
              "requisito_historia": "Se requiere crear el boton de login de la app",
              "complejidad": "Media",
              "Conocimiento": "Senior",
              "Complejidad_Pruebas": "Alta",
              "Impacto_solucion": "Alto",
              "Reusabilidad": "Alta",
              "Tasa_horas_dia": "7",
              "Tamanio_implementacion": "Medio",
              "Complejidad_investigacion": "Bajo",
              "Tipo_implementacion": "Tradicional",
              "Puntos": "10",
              "Cantidad_horas": "30"
            }
          ]
        },
        {
          "id_proyecto": "py_1",
          "datos": [
            {
              "id": "2",
              "requisito_historia": "Se requiere crear boton logout",
              "complejidad": "Media",
              "Conocimiento": "Senior",
              "Complejidad_Pruebas": "Alta",
              "Impacto_solucion": "Alto",
              "Reusabilidad": "Alta",
              "Tasa_horas_dia": "7",
              "Tamanio_implementacion": "Medio",
              "Complejidad_investigacion": "Bajo",
              "Tipo_implementacion": "Tradicional",
              "Puntos": "10",
              "Cantidad_horas": "30"
            }
          ]
        }
      ]
    }
        
    return estimaciones


