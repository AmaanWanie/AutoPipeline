from pretrained import *

loader = ModelLoader(task='image', name='resnet', version="50", pretrained=False)
model = loader.load_model()