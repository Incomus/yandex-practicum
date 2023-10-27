import tensorflow as tf


(features_train, target_train), (features_test, target_test) = tf.keras.datasets.fashion_mnist.load_data()
assert features_train.shape == (60000, 28, 28)
assert features_test.shape == (10000, 28, 28)
assert target_train.shape == (60000,)
assert target_test.shape == (10000,)




features_train = features_train / 255
features_test = features_test / 255



model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Conv2D(filters=3, kernel_size=(5, 5),
                 activation="tanh", input_shape=(features_test.shape[1], features_test.shape[1], 1)))
model.add(tf.keras.layers.AvgPool2D(pool_size=(2, 2)))
model.add(tf.keras.layers.Conv2D(filters=9, kernel_size=(5, 5),
                 activation="tanh"))
model.add(tf.keras.layers.AvgPool2D(pool_size=(2, 2)))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(units=30, activation='tanh'))
model.add(tf.keras.layers.Dense(units=15, activation='tanh'))
model.add(tf.keras.layers.Dense(units=10, activation='softmax'))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
                  metrics=['acc'])
model.summary()


model.fit(features_train, target_train,
              validation_data=(features_test, target_test),
              epochs=20, verbose=2, shuffle=True)

