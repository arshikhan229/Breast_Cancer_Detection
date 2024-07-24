import matplotlib.pyplot as plt

def visualize_prediction(img_path, predicted_mask):
    img_array = plt.imread(img_path)
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(img_array)

    plt.subplot(1, 2, 2)
    plt.title("Predicted Mask")
    plt.imshow(predicted_mask, cmap='gray')

    plt.show()

def describe_result(original_image, predicted_mask):
    affected_area_percentage = (np.sum(predicted_mask) / predicted_mask.size) * 100
    description = (
        f"The original image has been processed, and the model has predicted a segmentation mask. "
        f"Approximately {affected_area_percentage:.2f}% of the image area is predicted to be affected."
    )
    print(description)
