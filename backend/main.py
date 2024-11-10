from fastapi import FastAPI
from data.preprocess import build_transforms, TransformConfig

app = FastAPI()

@app.post("/get_transforms")
def get_transforms(config: TransformConfig):
  return build_transforms(config)
