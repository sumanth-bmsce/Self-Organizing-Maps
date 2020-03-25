# Self-Organizing-Maps
A Self Organizing Maps (SOM) or Kohonen Network is a type of Artificial Neural Network that is trained using clustering of datasets. This repo implements SOM using MiniSOM library applied on Iris Dataset and outputs the confusion matrix and clustering accuracy

## Advantages of Self Organizing Maps over other clusetering algorithms ##

* SOM is superior in dealing with processes which have multiple optima
* SOM offers the opportunity for an early exploration of the search space, and as the process continues it gradually narrows the search. By the end of the search process (providing the neighborhood radius decreases to zero) the SOM is exactly the same as k-means, which allows for a minimization of the distances between the data points and the cluster centers. 

## Self Organizing Maps Flow Diagram ##

## Clustering Accuracy ##
The confusion matrix and the clustering accuracy for SOM applied on IRIS Dataset is shown in the image below. The clustering accuracy obtained is 90.66 %


![picture alt](https://github.com/sumanth-bmsce/Self-Organizing-Maps/blob/master/SOM_Iris_Result.png "Cf Matrix and accuracy")
