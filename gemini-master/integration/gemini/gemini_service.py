from google import genai

class GeminiService:
    def __init__(self, api_key="AIzaSyDCYPPwel7EAnWscN38-afrNoSzifc0zA8"):
        self.client = genai.Client(api_key=api_key)
        
    def generate_text(self, prompt, model="gemini-2.0-flash"):
        try:
            response = self.client.models.generate_content(
                model=model, 
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"Erro ao gerar resposta: {str(e)}"