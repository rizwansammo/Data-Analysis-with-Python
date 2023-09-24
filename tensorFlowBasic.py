import tensorflow as tf
import numpy as np

# Generate some random data for demonstration
np.random.seed(0)
bedrooms = np.random.randint(1, 5, size=100)
prices = 100000 + 20000 * bedrooms + np.random.randn(100) * 10000

# Define the model architecture
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Convert the data to TensorFlow tensors
bedrooms_tf = tf.convert_to_tensor(bedrooms, dtype=tf.float32)
prices_tf = tf.convert_to_tensor(prices, dtype=tf.float32)

# Train the model
model.fit(bedrooms_tf, prices_tf, epochs=100)

# Make predictions
predictions = model.predict(bedrooms_tf)

# Print the learned parameters
print("Learned parameters:")
print(f"Weight: {model.layers[0].get_weights()[0][0][0]}")
print(f"Bias: {model.layers[0].get_weights()[1][0]}")
