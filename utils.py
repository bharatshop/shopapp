import whisper

model = whisper.load_model("tiny")

def trascribe(audio):
  text = model.transcribe(audio)
  return text['text']

print(trascribe('/workspaces/shopapp/audio.wav'))