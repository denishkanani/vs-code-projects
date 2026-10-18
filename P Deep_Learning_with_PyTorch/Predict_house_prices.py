import torch
import torch.nn as nn

# normalized data
X = torch.tensor([[1.0],[1.5],[2.0]])
y = torch.tensor([[1.0],[1.5],[2.0]])

model = nn.Linear(1,1)

loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(1000):

    pred = model(X)
    loss = loss_fn(pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print("Weight:", model.weight.item())
print("Bias:", model.bias.item())

prediction = model(torch.tensor([[2.5]]))
print("Prediction:", prediction.item())