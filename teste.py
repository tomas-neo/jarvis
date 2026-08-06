import speech_recognition as sr

print("Buscando portas de áudio no sistema...\n")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"[{index}] {name}")
