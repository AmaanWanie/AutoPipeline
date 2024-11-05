from trainer import trainer as t
import torch

model =  torch.nn.Linear(1, 1)
train_loader = torch.utils.data.DataLoader(torch.utils.data.TensorDataset(torch.randn(100,1), torch.randn(100,1)), batch_size=10)
val_loader = torch.utils.data.DataLoader(torch.utils.data.TensorDataset(torch.randn(100,1), torch.randn(100,1)), batch_size=10)


trainer,logs = t(model, train_loader, val_loader, torch.nn.MSELoss(), torch.optim.SGD(model.parameters()) )
print(logs)
model =  torch.nn.Sequential(torch.nn.Linear(1, 1), torch.nn.ReLU(),
                             torch.nn.Linear(1, 1), torch.nn.ReLU(),
                             torch.nn.Linear(1, 1))
trainer,logs = t(model, train_loader, val_loader, torch.nn.MSELoss(), torch.optim.SGD(model.parameters()) )

print(logs)