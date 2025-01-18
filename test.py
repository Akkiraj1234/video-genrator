import asyncio
from gtts import gTTS
from googletrans import Translator

async def translate_and_generate_speech():
    # Initialize the translator
    translator = Translator()

    # Text in English
    text = "Hello, I am Akki"

    # Translate to Hindi (await the coroutine)
    translated = await translator.translate(text, src='en', dest='hi')
    translated_text = translated.text

    print(f"Translated Text: {translated_text}")

    # Generate speech in Hindi
    tts = gTTS(text=translated_text, lang='hi')
    tts.save("hello_in_hindi.mp3")
    print("Speech saved as hello_in_hindi.mp3")

# Run the async function
asyncio.run(translate_and_generate_speech())
