import whisper

model = whisper.load_model("base")

def transcribe(audiopath):
  text = model.transcribe(audiopath, fp16=False)
  return text['text']

print(transcribe('/workspaces/shopapp/audio.wav'))