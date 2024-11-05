from pretrained import *

loader = ModelLoader(task='image', name='resnet', version="50", pretrained=False).load_model()
loader = ModelLoader(task='audio', name='wav2vec', version="2", pretrained=False).load_model()
loader = ModelLoader(task='text', name='gpt2', version="medium", pretrained=False).load_model()
loader = ModelLoader(task='text', name='bert', version="base", pretrained=False).load_model()
loader = ModelLoader(task='text', name='roberta', version="base", pretrained=False).load_model()
loader = ModelLoader(task='text', name='distilbert', version="base", pretrained=False).load_model()
