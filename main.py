import speech_recognition as sr
import subprocess
from datetime import datetime
import sys, os

# Código avançado para calar a boca dos avisos do ALSA no Linux
sys.stderr = open(os.devnull, 'w')
import pyaudio
sys.stderr = sys.__stderr__

def executar_comando(comando):
    if "horas" in comando or "que horas são" in comando:
        agora = datetime.now().strftime("%H:%M")
        print(f"🤖 Jarvis: Agora são {agora}.")
        
    elif "abrir pasta" in comando or "arquivos" in comando:
        print("🤖 Jarvis: Abrindo os arquivos...")
        subprocess.Popen(['xdg-open', '.'])
        
    elif "terminal" in comando:
        print("🤖 Jarvis: Abrindo um novo terminal...")
        subprocess.Popen(['x-terminal-emulator'])

    elif "desligar" in comando or "encerrar" in comando:
        print("🤖 Jarvis: Desligando o sistema. Até logo!")
        exit()
        
    else:
        print(f"🤖 Jarvis: Comando não reconhecido: '{comando}'")

if __name__ == "__main__":
    print("Iniciando o sistema Jarvis...")
    recognizer = sr.Recognizer()
    
    # Abre o microfone UMA única vez
    with sr.Microphone() as source:
        print("Calibrando o ruído ambiente... Aguarde 1 segundo.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        # O Loop agora roda com o microfone já aberto
        while True:
            print("\n🎙️ Jarvis ouvindo... Pode falar!")
            try:
                audio = recognizer.listen(source, timeout=5)
                print("Processando...")
                
                texto = recognizer.recognize_google(audio, language='pt-BR').lower()
                print(f"✅ Você disse: '{texto}'")
                
                executar_comando(texto)
                
            except sr.UnknownValueError:
                pass # Silencia o erro de quando você não fala nada
            except sr.WaitTimeoutError:
                pass # Apenas reinicia o loop se passar 5 segundos em silêncio
            except Exception as e:
                print(f"❌ Erro de conexão ou inesperado: {e}")
