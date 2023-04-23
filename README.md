# Nepali Cash Detection and Recognition Using Transfer Learning and InceptionV3
This project focuses on detecting and recognizing Nepali cash using transfer learning and the InceptionV3 model. The model achieved 91% accuracy on both test and validation data.

## Dataset
The dataset used in this project consists of images of Nepali cash denominations. The dataset contains seven classes, namely:

* fifty
* five
* fivehundred
* hundred
* ten
* thousand
* twenty

## Model
Transfer learning was used to train the model using the InceptionV3 architecture. The model was trained on the dataset for 10 epochs with a batch size of 64. The model achieved an accuracy of 91% on both test and validation data.

## Results
The model achieved an accuracy of 91% on both test and validation data. The confusion matrix for the model is shown below:

<img src = "./evaluation-images/confusion-matrix.png">


A confusion matrix is a table that is often used to evaluate the performance of a classification model. The matrix compares the actual class labels of the test data with the predicted labels given by the model.

A confusion matrix typically has rows representing the true labels and columns representing the predicted labels. Each element of the matrix represents the count or number of instances that belong to a particular combination of true and predicted labels.

In the example matrix given above, the true labels are: fifty, five, fivehundred, hundred, ten, thousand, twenty. The predicted labels are the same.

The diagonal of the matrix shows the number of true positives (i.e., correct predictions) for each class, and the off-diagonal elements show the number of false positives (i.e., incorrect predictions) for each class.

For example, the element in the first row and first column represents the number of instances that truly belong to the class 'fifty' and were predicted as 'fifty' by the model. In this case, the value is 66. 

Again we can see that there are 5 instances of 'hundred' that were misclassified as 'fivehundred' by the model. 

By analyzing the confusion matrix, we can evaluate the performance of the model and identify the areas where the model is making mistakes. 

For example, in the above matrix, we can see that the model is confusing the classes and has misclassified 14 instances of 10 as 500. We can use this information to improve the model's performance, for example by increasing the amount of training data or tweaking the model's hyperparameters.

### Training and Validation Accuracy
<img src = "./evaluation-images/train_val_acc.png">

In this example, the model is being trained and evaluated for 10 epochs. During training, the model is being optimized by minimizing the loss and maximizing the accuracy.

After each epoch, the model's performance is evaluated on a validation dataset, which is different from the training dataset. This helps to check if the model is overfitting to the training data or if it's learning general patterns that can be applied to new data.

The training accuracy refers to the accuracy of the model on the training dataset after each epoch. It indicates how well the model is learning the patterns in the training data.

The validation accuracy refers to the accuracy of the model on the validation dataset after each epoch. It indicates how well the model is generalizing to new data.

In this example, we can see that the model starts with a training accuracy of 0.7324 and a validation accuracy of 0.85 in the first epoch. This means that the model is performing better on the training dataset than the validation dataset, indicating that it may be overfitting.

However, as the number of epochs increases, we can see that the validation accuracy also increases, reaching a maximum of 0.9290 in the ninth epoch. This suggests that the model is learning more general patterns that can be applied to new data.

In the last epoch, we can see that the training accuracy is 0.9495, while the validation accuracy drops to 0.9043. This indicates that the model may be overfitting to the training data, and further training may not improve its performance on new data.


### Training and validation loss
<img src = "./evaluation-images/train_val_loss.png">

In the context of a machine learning model, the training and validation loss are measures of how well the model is performing during the training and validation phases, respectively.

The loss function is a measure of how well the model is able to predict the correct output. During training, the model is adjusted to minimize this loss. A low training loss indicates that the model is fitting the training data well, whereas a high training loss indicates that the model is not fitting the data well.

Validation loss is the loss computed on a set of data that is not used for training, and it is used to assess how well the model is generalizing to new data. If the validation loss is low, it indicates that the model is performing well on unseen data. If the validation loss is much higher than the training loss, it may indicate that the model is overfitting the training data and is not generalizing well.

In the example given, we can see that the training loss and accuracy decrease and increase respectively as the epochs increase, while the validation loss and accuracy fluctuate. The decrease in training loss and increase in training accuracy indicates that the model is fitting the training data better with each epoch.

## Conclusion
In conclusion, this project has demonstrated the effectiveness of transfer learning and the InceptionV3 model for detecting and recognizing Nepali cash denominations with an accuracy of 91%.


# Streamlit web application
To run the application, you need to have Streamlit installed on your computer. If you don't have Streamlit installed, you can install it by running the following command in your terminal or command prompt:

```bash
pip install streamlit
```
Once Streamlit is installed, navigate to the directory where your main.py file is located using your terminal or command prompt. Then, run the command:

```bash
streamlit run main.py
```

This should start the Streamlit server and open the web application in a new tab in your default web browser.

<img src = "./streamlit-output/streamlit-home.png">

Now Upload the Images inside `image-data-inference`

<img src = "./streamlit-output/inference-1.png">

Another Example
<img src = "./streamlit-output/inference-2.png">

# Note
The Streamlit application also has the capability to audibly identify the type of banknote.







