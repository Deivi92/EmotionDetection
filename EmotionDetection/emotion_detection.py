import requests

def emotion_detection(text_to_analyze):
    # URL y encabezados de la API de Watson NLP
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    # El cuerpo de la solicitud en formato JSON
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        # Realizar la solicitud POST a la API
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Verificar si hubo un error en la solicitud

        # Obtener el resultado en formato JSON
        result = response.json()

        # Imprimir la respuesta completa de la API para diagnóstico
        print("Respuesta completa de la API:", result)

        # Traducir las emociones del inglés al español
        emociones_traducidas = {
            "anger": "ira",
            "disgust": "desagrado",
            "fear": "miedo",
            "joy": "alegría",
            "sadness": "tristeza"
        }

        # Extraer las emociones con su puntuación
        emociones = result['emotionPredictions'][0]['emotion']

        # Traducir las emociones
        emociones_en_espanol = {emociones_traducidas.get(key, key): value for key, value in emociones.items()}

        # Calcular la emoción dominante en español
        emocion_dominante = max(emociones_en_espanol, key=emociones_en_espanol.get, default="Ninguna emoción encontrada")
        emociones_en_espanol["emocion_dominante"] = emocion_dominante

        # Devolver solo las emociones con sus puntuaciones en español
        return emociones_en_espanol

    except requests.exceptions.RequestException as e:
        # Manejar cualquier error de solicitud
        return f"Error al llamar al servicio: {e}"

    except Exception as e:
        # Manejar cualquier otro error inesperado
        return f"Error inesperado: {e}"
