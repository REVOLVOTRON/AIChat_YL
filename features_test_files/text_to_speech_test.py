from murf import Murf

client = Murf(
    api_key="ap2_8a76f382-76e3-4aa8-8209-77cff30d752c" # Not required if you have set the MURF_API_KEY environment variable
)

res = client.text_to_speech.generate(
    text="Привет старый пердун",
    voice_id="en-US-terrell",
)

print(res.audio_file)



    

"НЕ БЕСПЛАТНО(((( НЕ УДОБНО(((("