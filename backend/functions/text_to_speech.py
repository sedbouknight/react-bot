import requests
from decouple import config

ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")

# Eleven Labs Text-to-Speech
def convert_text_to_speech(message):
    # Define data {Body}
    body = {
        "text": message,
        "voice_settings":{
            "stability": 0,
            "similarity_boost": 0,
        }
    }

    # Define Voices
    voice_rachel = "21m00Tcm4TlvDq8ikWAM"
    voice_dave = "CYw3kZ02Hs0563khs1Fj"
    voice_daniel = "onwK4e9ZLuTAKqWW03F9"

    # Constructing Headers and Endpoint
    headers = {"xi-api-key": ELEVEN_LABS_API_KEY, "Content-Type": "application/json", "accept": "audio/mpeg"}
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_daniel}"

    # Send request
    try:
        response = requests.post(endpoint, json=body, headers=headers)
    except Exception as e:
        return

    #Handle Response
    if response.status_code == 200:
        return response.content
    else:
        return