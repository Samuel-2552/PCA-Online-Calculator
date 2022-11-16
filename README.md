#**Principal Component Analysis**

A front end devlopment for PCA. (Mini Project) Details Given below

**Explanation:** 

	The principal component analysis is a dimensionality reduction technique, which comes under the feature extraction methods. It is an unsupervised method to extract features from data into new feature space with less no of dimensions. 
  
We have developed a python code for principal component analysis in which when a dataset is passed can be reduced to number of components as per the user’s desire. But to make it easy even for non-coders we have developed a website that makes it all the more easy for user to interact with it. 

The user just needs to upload the data in the correct format and answer some questions related to dataset, like whether there is column name on the dataset or not, whether there is a label column or not, whether he wants to visualize his dataset and whether the user wants to apply normalization, standardization or just pass the normalized values and finally how many components the user wants to reduce the original dataset to.

After answering all this the user needs to upload the dataset and press the submit button which takes less than 2 seconds to process the data and plot it which can be downloaded and provides the Eigen values and Eigen vectors for the number of components it has been reduced to.


**Source Code for PCA:**

The source code for this project is provided in this GitHub Link below:

https://github.com/Samuel-2552/PCA-Online-Calculator 

There are 3 folders and 3 files in the main branch.

•	The app.py file is python file which runs flask with the PCA code.
•	The Procfile and the requirements.txt file are used for heroku deployment.
•	The PCA folder has the python code for PCA and 3 different datasets.
•	The templates folder has the index.html file in which we have developed the code for front end.
•	The static folder has the style.css file and the script.js file necessary for the front development design and the required png images.

This website has been deployed in heroku platform and can be accessed through the link provided below:

https://bit.ly/sam-pca

Output looks like this:

 ![image](https://user-images.githubusercontent.com/104893913/202197897-9fc6f805-a808-4fd3-b681-e0fb388210bf.png)
 

![image](https://user-images.githubusercontent.com/104893913/202197930-ff7cbe96-98db-463f-b442-9b8c612f1921.png)

![image](https://user-images.githubusercontent.com/104893913/202197952-69eae6fa-88a9-4bef-9f23-8307ef1c87dc.png)

![image](https://user-images.githubusercontent.com/104893913/202197992-f105b48e-4daa-417b-b727-151876f85398.png)

![image](https://user-images.githubusercontent.com/104893913/202198039-0054d18a-61b9-49a5-96fb-b2ca8ea95acb.png)

![image](https://user-images.githubusercontent.com/104893913/202198071-c7ded08e-f8ab-4df8-81e8-e8096415e69b.png)

![image](https://user-images.githubusercontent.com/104893913/202198095-27e473bf-93ae-4756-a71d-f6efabc30751.png)
