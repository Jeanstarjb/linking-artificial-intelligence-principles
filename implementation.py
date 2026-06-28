import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset

# Define a simple dataset class
class AIDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

# Define a simple neural network to link AI principles
class AIPrinciplesLinker(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(AIPrinciplesLinker, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.softmax(x)
        return x

# Training function
def train_model(model, dataloader, criterion, optimizer, epochs=10):
    for epoch in range(epochs):
        for data, labels in dataloader:
            data, labels = data.float(), labels.long()
            optimizer.zero_grad()
            outputs = model(data)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item()}")

# Evaluation function
def evaluate_model(model, dataloader):
    correct = 0
    total = 0
    with torch.no_grad():
        for data, labels in dataloader:
            data, labels = data.float(), labels.long()
            outputs = model(data)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    accuracy = 100 * correct / total
    print(f"Accuracy: {accuracy}%")

if __name__ == '__main__':
    # Dummy data to simulate AI principles and their links
    np.random.seed(42)
    torch.manual_seed(42)

    # Simulate 10 AI principles with 5 features each
    num_principles = 100
    num_features = 5
    num_classes = 3  # Assume 3 categories of principles
    data = np.random.rand(num_principles, num_features)
    labels = np.random.randint(0, num_classes, num_principles)

    # Convert to PyTorch tensors
    dataset = AIDataset(torch.tensor(data), torch.tensor(labels))
    dataloader = DataLoader(dataset, batch_size=10, shuffle=True)

    # Define model, loss, and optimizer
    input_size = num_features
    hidden_size = 16
    output_size = num_classes
    model = AIPrinciplesLinker(input_size, hidden_size, output_size)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    # Train the model
    train_model(model, dataloader, criterion, optimizer, epochs=20)

    # Evaluate the model
    evaluate_model(model, dataloader)