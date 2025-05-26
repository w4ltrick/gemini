import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .gemini_service import GeminiService

def index(request):
    context = {
        'response': None
    }
    
    if request.method == 'POST':
        prompt = request.POST.get('prompt', '')
        model = request.POST.get('model', 'gemini-2.0-flash')
        
        if prompt:
            service = GeminiService()
            response = service.generate_text(prompt, model=model)
            
            context = {
                'prompt': prompt,
                'model': model,
                'response': response
            }
    
    return render(request, 'index.html', context)

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            prompt = data.get('message', '')
            model = data.get('model', 'gemini-2.0-flash')
            
            # Use a mesma função que você já tem para gerar texto
            from google import genai
            client = genai.Client(api_key="AIzaSyDCYPPwel7EAnWscN38-afrNoSzifc0zA8")
            response = client.models.generate_content(
                model=model, 
                contents=prompt
            )
            
            return JsonResponse({
                'response': response.text
            })
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            }, status=400)
    
    return JsonResponse({'error': 'Método não permitido'}, status=405)

