# KNN From Scratch
This project will predict person who have cancer.
## Requirements
* Numpy
* Pandas
# Linear Regression From Scratch
## Requirements
* Python 3
* Numpy
* Pandas

## Documentation
there are 2 programs 

* main.py
---
this is main program. How to use just type python3 main.py

---

* knn.py
1. preprocess funcion

---

This function is about cleaning and prepare dataset. The dataset used is breast cancer dataset.

---

2. modus function

---
Find mode value in K neighbor values

---

3. euclidean_distance function

---

calculate distance every single features

---

4. get_neighbors function

---

calculate train test data using euclidean_distance function. Value is top priority from K members, then the mode will be searched refers to modus function.

---

5. train_test_split function
---

spliting data into train dan test

---

6. evaluate function
---

Evaluating test data to find accuracy. Accuracy is obtained from (TP/(TP+FP))*100. TP is correctly predict and FP is the oposite

---

## Additional infomation

* link dataset : https://www.kaggle.com/uciml/breast-cancer-wisconsin-data

* For implementing your own dataset, first do the preparation and cleaning data. Make sure atributes in numpy array format. Then you can replace X_train,X_test with your own data.