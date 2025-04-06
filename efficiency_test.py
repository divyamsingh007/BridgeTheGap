import tensorflow as tf
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load your trained model
model = tf.keras.models.load_model('my_last_model.h5')

# ⚠️ Load dataset with one-hot encoded labels
test_ds = tf.keras.utils.image_dataset_from_directory(
    'data/test',              # Path to your test folder
    image_size=(64, 64),
    batch_size=32,
    shuffle=False,
    label_mode='categorical'     # ⚠️ Makes labels one-hot encoded
)

# Extract class names
class_names = test_ds.class_names

# Get true labels
y_true = np.concatenate([y.numpy() for x, y in test_ds], axis=0)
y_true_labels = np.argmax(y_true, axis=1)  # Convert one-hot back to class index

# Get model predictions
y_pred_probs = model.predict(test_ds)
y_pred_labels = np.argmax(y_pred_probs, axis=1)

# Evaluate model
loss, acc = model.evaluate(test_ds)
print(f"\n✅ Test Accuracy: {acc * 100:.2f}%")
print(f"🧮 Test Loss: {loss:.4f}")

# Classification report
print("\n📋 Classification Report:")
print(classification_report(y_true_labels, y_pred_labels, target_names=class_names))

# Confusion matrix
cm = confusion_matrix(y_true_labels, y_pred_labels)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='g', cmap='Blues',
            xticklabels=class_names, yticklabels=class_names)
plt.title("📊 Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.tight_layout()
plt.show()
