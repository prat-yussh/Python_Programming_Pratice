import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam

# ===============================
# DATA GENERATORS
# ===============================

train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

val_datagen = ImageDataGenerator(rescale=1./255)

test_datagen = ImageDataGenerator(rescale=1./255)

train_set = train_datagen.flow_from_directory(
    'dataset/train',
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    shuffle=True
)

val_set = val_datagen.flow_from_directory(
    'dataset/validation',
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    shuffle=False
)

test_set = test_datagen.flow_from_directory(
    'dataset/test',
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    shuffle=False
)

# ===============================
# CNN MODEL
# ===============================

cnn = Sequential([
    Conv2D(32, 3, activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D(2, 2),

    Conv2D(64, 3, activation='relu'),
    MaxPooling2D(2, 2),

    Conv2D(128, 3, activation='relu'),
    MaxPooling2D(2, 2),

    Dropout(0.5),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')
])

cnn.compile(
    optimizer=Adam(learning_rate=1e-4),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

cnn.summary()

# ===============================
# TRAINING
# ===============================

history = cnn.fit(
    train_set,
    epochs=50,
    validation_data=val_set,
    callbacks=[
        tf.keras.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=5,
            restore_best_weights=True
        )
    ]
)

# ===============================
# TEST EVALUATION
# ===============================

test_loss, test_acc = cnn.evaluate(test_set)
print(f"\nTest Accuracy: {test_acc:.4f}")

# ===============================
# SINGLE IMAGE PREDICTION
# ===============================

img_path = 'prediction/deepfake1.jpg'

img = tf.keras.utils.load_img(
    img_path,
    target_size=(224, 224)
)

img_array = tf.keras.utils.img_to_array(img)
img_array = img_array / 255.0
img_array = np.expand_dims(img_array, axis=0)

prediction = cnn.predict(img_array)

class_names = list(train_set.class_indices.keys())
predicted_class = class_names[int(prediction[0][0] > 0.5)]

print("\nPrediction probability:", prediction[0][0])
print("Predicted class:", predicted_class)

plt.imshow(img)
plt.axis('off')
plt.show()
