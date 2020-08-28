import pandas
import numpy
import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
data = pandas.read_csv("pokemon.csv")
Y = data['Name']
y_array = numpy.array(Y)
images = []
y_final = []
le = LabelEncoder()
le.fit(y_array)
for i in y_array:
       img = cv2.imread("images/"+i+".png")
       try:
        img = cv2.resize(img,(70,70))
        cv2.imshow("img",img)
        cv2.waitKey(1)
        y_final.append(le.transform([i]))
        images.append(img)
       except:
        continue;



y_array = numpy.array(y_final)
images = numpy.array(images)
images = images.astype('float32')
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(70,70,3)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(images, y_array, epochs=10)
