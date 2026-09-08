# Jarvis

Código de teste para tentar fazer um app de assistente de voz: escuta o
microfone, tenta reconhecer uma palavra de ativação e interpretar um comando
simples a partir da fala.

## Requisitos

- Python 3
- [`SpeechRecognition`](https://pypi.org/project/SpeechRecognition/)
- [`PyAudio`](https://pypi.org/project/PyAudio/)
- Microfone configurado no sistema

```bash
pip install SpeechRecognition PyAudio
```

## Uso

```bash
python main.py
```

`teste.py` lista os microfones disponíveis no sistema.
