import tkinter as tk
from tkinter import filedialog, messagebox
import ffmpeg
import whisper
import os

# Função para extrair áudio do vídeo
def extract_audio(video_path, audio_output):
    ffmpeg.input(video_path).output(audio_output).run()

# Função para transcrever o áudio
def transcribe_audio(audio_path):
    model = whisper.load_model("base")  # Escolha do modelo Whisper, pode usar 'medium', 'large', etc.
    result = model.transcribe(audio_path)
    return result['text']

# Função que executa todo o processo: extrair o áudio e transcrever
def process_video():
    video_path = filedialog.askopenfilename(title="Selecione o vídeo", filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")])
    if not video_path:
        return
    
    # Caminho temporário para salvar o áudio extraído
    audio_path = "temp_audio.wav"
    
    # Extrai o áudio do vídeo
    extract_audio(video_path, audio_path)
    
    # Faz a transcrição do áudio
    transcription = transcribe_audio(audio_path)
    
    # Mostra a transcrição ao usuário
    messagebox.showinfo("Transcrição", transcription)
    
    # Remove o arquivo de áudio temporário
    os.remove(audio_path)

# Configuração da interface gráfica com Tkinter
app = tk.Tk()
app.title("Vídeo-to-Text")
app.geometry("300x200")

# Rótulo para instruir o usuário
label = tk.Label(app, text="Selecione um vídeo para transcrever:")
label.pack(pady=20)

# Botão para selecionar o vídeo
btn = tk.Button(app, text="Escolher vídeo", command=process_video)
btn.pack(pady=10)

# Inicia a interface gráfica
app.mainloop()
