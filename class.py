import torch.nn as nn
import torch.nn.functional as F

class MLPNet(nn.Module):
    def __init__(self):
        super(MLPNet, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 50)
        # Define the output layer
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        # Flatten the input image
        x = x.view(-1, 28 * 28)
        # Pass through the hidden layer with ReLU activation
        x = F.relu(self.fc1(x))
        # Output layer
        x = self.fc2(x)

        return x
    
    # %%time
mlp_net = MLPNet()
train_loss, train_acc, test_loss, test_acc = execution(mlp_net, epochs=100, trainset_size=1000)

#%%time
mlp_net = MLPNet()
train_loss, train_acc, test_loss, test_acc = execution(mlp_net, epochs=10, trainset_size=50000)

