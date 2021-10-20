import os
texts, train_texts, val_texts, train_labels = [], [], [], []
train_root = "Train_Textual/"
val_root = "Validation/"
test_root = "Test_Intuitive/"
textual = []
intuitive = []
test_labels = []
for filename in os.listdir(train_root):
    text = open(train_root+filename).read()
    texts.append(text)
    train_texts.append(text)
    textual.append(filename.split('_')[-1].split('.')[0])
    if filename[0] == 'U' or filename[0] == 'N':
        train_labels.append(0)
    else:
        train_labels.append(1)
for filename in os.listdir(test_root):
    text = open(test_root+filename).read()
    texts.append(text)
    train_texts.append(text) 
    intuitive.append(filename.split('_')[-1].split('.')[0])
    if filename[0] == 'U' or filename[0] == 'N':
        test_labels.append(0)
    else:
        test_labels.append(1)
print(textual)
print(intuitive)
intersection = list(set(textual) & set(intuitive))
print(len(intersection))
#print(train_labels)