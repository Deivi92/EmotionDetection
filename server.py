from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detection  # Asegúrate de que esta importación sea correcta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Asumiendo que tienes un archivo index.html en templates/

@app.route('/analyze_emotion', methods=['POST'])
def analyze_emotion():
    if request.method == 'POST':
        text_to_analyze = request.form['text']  # Obtener el texto del formulario

        # Llamar a la función emotion_detection para obtener las emociones
        emociones = emotion_detection(text_to_analyze)

        # Devolver las emociones como una respuesta JSON
        return jsonify(emociones)

if __name__ == '__main__':
    app.run(debug=True)
