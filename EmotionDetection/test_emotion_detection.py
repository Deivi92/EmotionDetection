import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    
    def test_anger(self):
        resultado = emotion_detector("Estoy realmente enojado por esto.")
        self.assertEqual(resultado['emocion_dominante'], 'ira')  # Asegurarte que la emoción detectada es 'ira'

    def test_disgust(self):
        resultado = emotion_detector("Me siento disgustado solo de oír sobre esto.")
        self.assertEqual(resultado['emocion_dominante'], 'desagrado')  # Asegurarte que la emoción detectada es 'desagrado'

    def test_fear(self):
        resultado = emotion_detector("Tengo mucho miedo de que esto suceda.")
        self.assertEqual(resultado['emocion_dominante'], 'miedo')  # Asegurarte que la emoción detectada es 'miedo'

    def test_sadness(self):
        resultado = emotion_detector("Estoy tan triste por esto.")
        self.assertEqual(resultado['emocion_dominante'], 'tristeza')  # Asegurarte que la emoción detectada es 'tristeza'
        
    def test_joy(self):
        resultado = emotion_detector("Me encanta esta nueva tecnología.")
        self.assertEqual(resultado['emocion_dominante'], 'alegría')  # Asegurarte que la emoción detectada es 'alegría'

if __name__ == "__main__":
    unittest.main()

