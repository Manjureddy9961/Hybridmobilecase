from django.shortcuts import render
from django.http import JsonResponse
import json
import os
import google.generativeai as genai

# Configure Gemini API
# NOTE: User needs to set GEMINI_API_KEY in environment variables or hardcode it here
GENAI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
if GENAI_API_KEY != "YOUR_API_KEY_HERE":
    genai.configure(api_key=GENAI_API_KEY)

def home(request):
    return render(request, 'index.html')

def technology(request):
    return render(request, 'technology.html')

def analytics(request):
    return render(request, 'analytics.html')

def battery(request):
    return render(request, 'battery.html')

def chatbot(request):
    return render(request, 'chatbot.html')

def profile(request):
    return render(request, 'profile.html')

def notifications(request):
    return render(request, 'notifications.html')

def chatbot_response(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '').lower()
            
            # Smart Local Mode (No API Key Required)
            if GENAI_API_KEY == "YOUR_API_KEY_HERE":
                
                # Knowledge Base
                knowledge = {
                    "price": "EnergyNest is priced at $40, offering premium value compared to standard cases ($3-$5) by adding unlimited battery life.",
                    "cost": "EnergyNest is priced at $40, offering premium value compared to standard cases ($3-$5) by adding unlimited battery life.",
                    "how": "It uses a hybrid system: Solar (light), Piezoelectric (movement), Acoustic (sound), and Thermoelectric (heat) generators to charge an internal battery.",
                    "work": "It uses a hybrid system: Solar (light), Piezoelectric (movement), Acoustic (sound), and Thermoelectric (heat) generators to charge an internal battery.",
                    "solar": "Our flexible Perovskite solar cells are 25% efficient and work even in indoor lighting.",
                    "compatible": "EnergyNest supports iPhone 12 and newer, as well as Samsung Galaxy S21 and newer models via Qi wireless charging.",
                    "iphone": "EnergyNest supports iPhone 12 and newer, as well as Samsung Galaxy S21 and newer models via Qi wireless charging.",
                    "samsung": "EnergyNest supports iPhone 12 and newer, as well as Samsung Galaxy S21 and newer models via Qi wireless charging.",
                    "safety": "It is 100% safe. Our Smart PMIC prevents overcharging, overheating, and reverse current.",
                    "safe": "It is 100% safe. Our Smart PMIC prevents overcharging, overheating, and reverse current.",
                    "buy": "You can order directly by clicking the 'Order Now' button in the menu.",
                    "order": "You can order directly by clicking the 'Order Now' button in the menu."
                }

                # Keyword Matching
                for key, answer in knowledge.items():
                    if key in user_message:
                        return JsonResponse({'response': answer})
                
                # Default Fallback
                return JsonResponse({'response': "I can help with **Price**, **Technology**, **Compatibility**, and **Safety**. Try asking: 'How does it work?' or 'What is the price?'"})

            # Gemini Logic (If API Key is set)
            model = genai.GenerativeModel('gemini-pro')
            chat = model.start_chat(history=[])
            context = "You are EnergyBot, an AI expert for EnergyNest. Answer technically and helpfully."
            response = chat.send_message(f"{context}\n\nUser: {user_message}")
            return JsonResponse({'response': response.text})
            
        except Exception as e:
            return JsonResponse({'response': f"Error: {str(e)}"}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=400)
