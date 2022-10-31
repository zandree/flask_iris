import torch
import numpy as np

# Criar um modelo de Rede Neural
class Net(torch.nn.Module):
  def __init__(self, input_size, hidden_size, output_size):
    super(Net, self).__init__()
    self.input_size = input_size
    self.hidden_size = hidden_size
    self.output_size = output_size
    self.fc1 = torch.nn.Linear(self.input_size, self.hidden_size) #full connected
    self.relu = torch.nn.ReLU() #(0, infinito)
    self.fc2 = torch.nn.Linear(self.hidden_size, self.output_size)
    self.sigmoid = torch.nn.Sigmoid() #(0, 1)
  def forward(self, x):
    hidden = self.fc1(x)
    relu = self.relu(hidden)
    output = self.fc2(relu)
    output = self.sigmoid(output)
    return output

def predict(dados):
    #dados = [larg_sepala, comp_sepala, larg_petala, comp_petala]
    entrada = torch.FloatTensor(dados)
    # print(entrada)
    # print(entrada.size())
    input_size = entrada.size()[0]
    hidden_size = 10
    output_size = 3
    modelo = Net(input_size, hidden_size, output_size)
    modelo.load_state_dict(torch.load('./modelo/iris.dat'))
    modelo.eval()
    y_pred = modelo(entrada) # rodar o modelo com os dados de entrada 
    y_pred = y_pred.detach().numpy()
    return y_pred
