import torch
import os
import util_instance
import datetime

# data

import numpy as np
import re


class Net(torch.nn.Module):
    def __init__(self, n_feature, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, 100)
        self.predict = torch.nn.Linear(100, n_output)

    def forward(self, x):
        out = self.hidden(x)
        out = torch.relu(out)
        out = self.predict(out)
        return out


def regress(dataset, email, in_id):
    ff = open(dataset).readlines()
    data = []
    for item in ff:
        out = re.sub(r"\s{2,}", " ", item).strip()
        data.append(out.split(" "))
    data = np.array(data).astype(float)

    Y = data[:, -1]
    X = data[:, 0:-1]

    X_train = X[0:496, ...]
    Y_train = Y[0:496, ...]
    X_test = X[496:, ...]
    Y_test = Y[496:, ...]

    # net

    net = Net(13, 1)

    # loss

    loss_func = torch.nn.MSELoss()

    # optimiter

    optimizer = torch.optim.Adam(net.parameters(), lr=0.01)  # 损失函数Adam

    # trainer

    for i in range(10000):
        x_data = torch.tensor(X_train, dtype=torch.float32)
        y_data = torch.tensor(Y_train, dtype=torch.float32)
        pred = net.forward(x_data)  # 前向运算 根据x计算pred
        pred = torch.squeeze(pred)
        loss_pred = loss_func(pred, y_data) * 0.001  # 计算loss
        # 优化器
        optimizer.zero_grad()  # 将参数置为零
        loss_pred.backward()  # backward反向传播
        optimizer.step()  # 更新参数


        # test
        x_data = torch.tensor(X_test, dtype=torch.float32)
        y_data = torch.tensor(Y_test, dtype=torch.float32)
        pred = net.forward(x_data)  # 前向运算 根据x计算pred
        pred = torch.squeeze(pred)

    path = f"C:/model/{email}/{in_id}"

    if not os.path.exists(path):
        os.makedirs(path)

    torch.save(net.state_dict(), f'{path}/model.pkl')
    ntime = str(datetime.datetime.now()).split(".")[0]
    ntime = datetime.datetime.strptime(ntime, '%Y-%m-%d %H:%M:%S')
    util_instance.update_info(in_id, ntime, 'end_time')
    util_instance.update_info(in_id, 2, 'state')
