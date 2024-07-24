from data_loader import LoadData
from preprocessing import preprocess_image
from model import unet_model
from predict import predict_image, describe_prediction
from visualize import visualize_prediction, describe_result

def main():
    framObjTrain = {'img': [], 'mask': []}
    framObjTrain = LoadData(framObjTrain, imgPath='/content/Dataset_BUSI_with_GT/benign', maskPath='/content/Dataset_BUSI_with_GT/benign')
    framObjTrain = LoadData(framObjTrain, imgPath='/content/Dataset_BUSI_with_GT/malignant', maskPath='/content/Dataset_BUSI_with_GT/malignant')

    model = unet_model()
    model.fit(framObjTrain['img'], framObjTrain['mask'], epochs=5, batch_size=32)

    image_path = "/content/Dataset_BUSI_with_GT/normal/normal (103).png"
    preprocessed_image = preprocess_image(image_path)
    prediction = predict_image(model, preprocessed_image)

    visualize_prediction(image_path, prediction)
    describe_result(image_path, prediction)

if __name__ == '__main__':
    main()
