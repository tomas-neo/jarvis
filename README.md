# Jarvis

Assistente de voz local em Python. Fica ouvindo o microfone, espera uma palavra de
ativação e executa um comando de uma lista restrita.

## Como funciona

1. Calibra o ruído ambiente do microfone por 1 segundo.
2. Fica escutando o áudio e transcreve com o Google Speech Recognition (`pt-BR`).
3. Se a frase contiver uma das palavras de ativação (`WAKE_WORDS`), o restante da
   frase é verificado contra a lista de comandos autorizados (`COMANDOS_AUTORIZADOS`).
4. Se o comando for reconhecido, a ação correspondente é executada.

### Palavras de ativação

`jarvis`, `charles`, `chaves`, `travis`, `davis`, `jardis`

### Comandos disponíveis

| Comando (palavra-chave) | Ação |
| --- | --- |
| `horas` | Fala a hora atual |
| `pasta` / `arquivos` | Abre o gerenciador de arquivos na pasta atual |
| `terminal` | Abre um novo terminal |
| `desligar` / `encerrar` | Encerra o programa |

## Requisitos

- Python 3
- [`SpeechRecognition`](https://pypi.org/project/SpeechRecognition/)
- [`PyAudio`](https://pypi.org/project/PyAudio/)
- Microfone configurado no sistema
- Conexão com a internet (o reconhecimento de fala usa a API do Google)

```bash
pip install SpeechRecognition PyAudio
```

## Uso

```bash
python main.py
```

Use `teste.py` para listar os índices e nomes dos microfones disponíveis no sistema,
caso seja necessário selecionar um dispositivo de áudio específico.
