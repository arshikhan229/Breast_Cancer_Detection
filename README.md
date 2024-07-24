# Breast Cancer Detection Using Ultrasound Images

This project aims to detect breast cancer using ultrasound images and a U-Net model for image segmentation. It includes data downloading, preprocessing, model training, prediction, and visualization.

## Project Structure

The project is divided into several modules for better organization and maintainability:

- `data_loader.py`: Handles data downloading and loading.
- `preprocessing.py`: Manages data preprocessing tasks such as handling missing values and scaling.
- `model.py`: Contains the U-Net model definition and training functions.
- `predict.py`: Includes functions for making predictions with the trained model.
- `visualize.py`: Functions for visualizing the predictions.
- `main.py`: Orchestrates the workflow of the entire project.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd breast_cancer_detection
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. (Optional) Set up Kaggle API credentials for downloading the dataset:
    ```sh
    mkdir ~/.kaggle
    cp kaggle.json ~/.kaggle/
    chmod 600 ~/.kaggle/kaggle.json
    ```

## Usage

1. Run the `main.py` script to execute the entire breast cancer detection pipeline:
    ```sh
    python main.py
    ```

## License

This project is licensed under the MIT License.
