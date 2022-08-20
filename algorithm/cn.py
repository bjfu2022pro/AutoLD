import torch
import torchvision.datasets as dataset
import torchvision.transforms as transforms
import torch.utils.data as data_utils
import os
import datetime
import util_instance, util_account


class CNN(torch.nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv = torch.nn.Sequential(
            torch.nn.Conv2d(1, 32, kernel_size=5, padding=2),
            torch.nn.BatchNorm2d(32),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2)
        )
        self.fc = torch.nn.Linear(14 * 14 * 32, 10)

    def forward(self, x):
        out = self.conv(x)
        out = out.view(out.size()[0], -1)
        out = self.fc(out)
        return out


#data
def cls(dset, email, in_id):                                        #可添加device选项,device = torch.device("device")
    train_data = dataset.MNIST(root=dset,
                            train=True,
                            transform=transforms.ToTensor(),
                            download=True)

    test_data = dataset.MNIST(root=dset,
                            train=False,
                            transform=transforms.ToTensor(),
                            download=False)

    #batchsize

    train_loader = data_utils.DataLoader(dataset=train_data,
                                        batch_size=64,
                                        shuffle=True)

    test_loader = data_utils.DataLoader(dataset=test_data,
                                        batch_size=64,
                                        shuffle=True)


    #net

    cnn = CNN()                                                         #cnn.to(device)

    #loss

    loss_func = torch.nn.CrossEntropyLoss()

    #optimizer

    optimizer = torch.optim.Adam(cnn.parameters(), lr=0.01)

    #training

    for epoch in range(5):
        for i, (images, labels) in enumerate(train_loader):
            outputs = cnn(images)                                       #images.to(device)
            loss = loss_func(outputs, labels)                           #labels.to(device)                                                            
                                                                        
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        print("epoch is {}, ite is {}/{}"
            ", loss is {}".format(epoch+1, i,
                                    len(train_data)//64,
                                    loss.item()))
        with torch.no_grad():
            #eval
            loss_test = 0
            accuracy = 0
            for i, (images, labels) in enumerate(test_loader):
                outputs = cnn(images)                                   #images.to(device) /n labels.to(device)
                loss_test += loss_func(outputs, labels)
                _, pred = outputs.max(1)
                accuracy += (pred == labels).sum().item()

            accuracy = accuracy / len(test_data)
            loss_test = loss_test / (len(test_data) // 64)

            print("epoch is {}, accuracy is {},"
                "loss test is {}".format(epoch+1,
                                        accuracy,
                                        loss_test.item()))


    #save
    
    path = f"static/model/{email}/{in_id}"

    if not os.path.exists(path):
        os.makedirs(path)

    torch.save(cnn.state_dict(), f'{path}/model.pkl')
    ntime = str(datetime.datetime.now()).split(".")[0]
    ntime = datetime.datetime.strptime(ntime, '%Y-%m-%d %H:%M:%S')
    util_instance.update_info(in_id, ntime, 'end_time')
    util_account.add_end(ntime, in_id)
    util_instance.update_info(in_id, 2, 'state')
    util_instance.cost_cacualte(in_id, email)