import sounddevice as sd

duration = 5  # tempo em segundos
fs = 4000  # 4000 amostras

print("gravando")
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()
print("fim da gravação")
# Salve a gravação como um arquivo de áudio
import scipy.io.wavfile
scipy.io.wavfile.write("recording4000.wav", fs, myrecording)