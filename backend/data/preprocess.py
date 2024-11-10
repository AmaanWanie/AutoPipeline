from torchvision import transforms as vtransforms
from torchaudio import transforms as atransforms
from torchtext import transforms as ttransforms
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional

app = FastAPI()

class TransformConfig(BaseModel):
  task: str
  transf: Optional[List[Dict[str, Dict]]] = None  # User-defined transforms

@app.post("/get_default_transforms")
def get_default_transforms(config: TransformConfig):
  task = config.task.lower()
  if task == 'image':
    return {"transforms": [
      {"Resize": {"size": [256, 256]}},
      {"ToTensor": {}}
    ]}
  elif task == 'audio':
    return {"transforms": [
      {"Resample": {"orig_freq": 44100, "new_freq": 16000}},
      {"MelSpectrogram": {"sample_rate": 16000, "n_mels": 128}},
      {"FrequencyMasking": {"freq_mask_param": 30}},
      {"TimeMasking": {"time_mask_param": 100}}
    ]}
  elif task == 'text':
    return {"transforms": [
      {"VocabTransform": {"vocab": "your_vocab"}},
      {"Truncate": {"max_seq_len": 128}}
    ]}
  else:
    raise HTTPException(status_code=400, detail="Invalid task")

@app.post("/build_transforms")
def build_transforms(config: TransformConfig):
  task = config.task.lower()
  transf = config.transf
  
  if transf is None:  # Use defaults if no user-defined transforms
    return get_default_transforms(config)
  
  # Return user-defined transforms directly as a JSON-compatible response
  return {"task": task, "transforms": transf}

###  possibly not a good way

# def get_default_transforms(task):
#   if task == 'image':
#     return vtransforms.Compose([
#       vtransforms.Resize((256, 256)),
#       vtransforms.ToTensor()
#     ])
#   elif task == 'audio':
#     return atransforms.Compose([
#       atransforms.Resample(orig_freq=44100, new_freq=16000),
#       atransforms.MelSpectrogram(sample_rate=16000, n_mels=128),
#       atransforms.FrequencyMasking(freq_mask_param=30),
#       atransforms.TimeMasking(time_mask_param=100)
#     ])
#   elif task == 'text':
#     return ttransforms.Compose([
#       ttransforms.VocabTransform(vocab),
#       ttransforms.Truncate(max_seq_len=128)
#     ])
#   else:
#     raise ValueError("Invalid task")

# def build_transforms(task, transf=None):
#   if transf is None:  # Use defaults if no user-defined transforms
#     return get_default_transforms(task)
    
#   if task == 'image':
#     return vtransforms.Compose(transf)
#   elif task == 'audio':
#     return atransforms.Compose(transf)
#   elif task == 'text':
#     return ttransforms.Compose(transf)
#   else:
#     raise ValueError("Invalid task")


