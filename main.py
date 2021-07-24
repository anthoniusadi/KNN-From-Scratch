
import knn
num_split=0.3
dataset=knn.preprocess()
x_train,x_test=knn.train_test_split(num_split,dataset)
hasil = knn.get_neighbors(x_train,x_test,3)
print('Prediction : ',hasil)
knn.evaluate(hasil,x_test)