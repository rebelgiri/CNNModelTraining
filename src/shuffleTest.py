import random
import numpy as np

from sklearn.utils import shuffle


numbers = [10, 20, 30, 40, 50, 60]
print ("Original list: ", numbers )
random.seed(4)
random.shuffle(numbers)
print("reshuffled list ", numbers)

# numbers = [10, 20, 30, 40, 50, 60]
random.seed(4)
random.shuffle(numbers)
print("reshuffled list ", numbers)

allData = [1, 2, 3, 4, 5, 6]
allLabel = [61, 62, 33, 85, 84, 53]

# shuffle data with randomness seed setting
data, label = shuffle(allData, allLabel, random_state=2)
train_data = [data, label]

print(train_data)



