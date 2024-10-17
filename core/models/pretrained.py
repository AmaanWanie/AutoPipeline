import torch
import torchvision.models as vmodels
import torchaudio.models as amodels

class PretrainedLoader:
    
    def __init__(self,framework="torch",task='image') -> None:
        self.framework = framework
        self.task = task

    def get_model(self,model_name,size,pretrained=True):
        if self.framework.lower() == "torch":
            return self._getpytorchmodel(model_name,size,pretrained)
        elif self.framework.lower() == "tf":
            return self._gettfmodel(model_name,size,pretrained)
        
    def _getpytorchmodel(self,name:str,size,pretrained):
        model = None
        if self.task == 'image':
            if name.lower() == 'resnet':
                model = vmodels.ResNet() # adjust to load pretriained of size
            if name.lower() == 'efficientnet':
                model = vmodels.EfficientNet() 
            if name.lower() == 'inceptionnet':
                model = vmodels.Inception3()
        
        if self.task == 'audio':
            if name.lower() == 'demucs':
                model = amodels.HDemucs() # adjust to load pretriained of size
            if name.lower() == 'wavernn':
                model = amodels.WaveRNN()
            if name.lower() == 'conformer':
                model = amodels.Conformer()

        return model
    

def _gettfmodel(self,name:str,size,pretrained):
    model = None
    pass
