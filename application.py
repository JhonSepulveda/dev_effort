from flask import Flask, request
import requests
from requests.auth import HTTPBasicAuth
import logging
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

sentry_logging = LoggingIntegration(
    level=logging.INFO,        # Capture info and above as breadcrumbs
    event_level=logging.ERROR  # Send errors as events
)

sentry_sdk.init(
    dsn="https://4723a1f9905343eea1583d9bf22ed64b@o1288684.ingest.sentry.io/6506103",
    integrations=[
        FlaskIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

app = Flask(__name__)


@app.route('/')
def home():    
    return 'Home'

# Esta entrada pertenece a la historia de usuario 
    #3- Presentaciòn de resultados.
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

            
# Esta entrada pertenece a la historia de usuario 
#1- Entrada de los datos.
@app.route('/estimaciones', methods=['POST'])
def add_estimaciones():    
    arr_data = {
          "requisito_historia": request.json['requisito_historia'],
          "complejidad": request.json['complejidad'],
          "Conocimiento": request.json['Conocimiento'],
          "Complejidad_Pruebas": request.json['Complejidad_Pruebas'],
          "Impacto_solucion": request.json['Impacto_solucion'],
          "Reusabilidad": request.json['Reusabilidad'],
          "Tasa_horas_dia": request.json['Tasa_horas_dia'],
          "Tamanio_implementacion": request.json['Tamanio_implementacion'],
          "Complejidad_investigacion": request.json['Complejidad_investigacion'],
          "Tipo_implementacion": request.json['Tipo_implementacion']
        }   
    return arr_data 

#Taller 2- branch : api-rest-feature 
@app.route('/api', methods=['GET'])
def get_api_data():    
    
    logging.error("Jhon Sepulveda:: Error progamado", extra=dict(bar=43))
    logging.exception("Jhon Sepulveda:: Excepcion")
    
    
    try:
        url = "http://api.open-notify.org/astros.json"
        response = requests.get(url, auth=HTTPBasicAuth('user', 'pass'))  
    except requests.exceptions.HTTPError as errh:
        #print(errh)
        logging.error(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
        logging.error(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
        logging.error(errt)
    except requests.exceptions.RequestException as err:
        print(err)
        logging.error(err)  
        
    return response.json()

# Esta entrada pertenece a la historia de usuario 
#2- Cálculo de esfuerzo de desarrollo de software.
def calculate_effort():
    
    #Se crea el cuerpo de este método, la lógica de implementación
    # se creara en base a la investigación del proyecto de grado.
    data = { "Numero de puntos" : "10",
             "Horas" : "30"
             }
    return data




                