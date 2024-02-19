1.Project Setup

1.Create any project folder in your system and copy the folder path.
2.Open Anaconda Powershell and first type your project folder drive name ex. e:
3.Then, cd E:\Data_Science_Project\Diamond_Price_Prediction
4.Now type code . as ex. E:\Data_Science_Project\Diamond_Price_Prediction code .
5.Then visual studio is opened in that folder. and you can create requirements.txt file and write pandas
6.Open the termainal and use cmd
7.type, conda deactivate
8.then type for creating the evironment, conda create -p venv python==3.8
9.After everything you can clear the screen, cls
10.Now we will activate the environment so that it refers to the current folder for the project., conda activate venv/
11.We can see that now we are inside the foler location.
12.Add the requirements inside requirements.txt and install from the cmd by typing, pip install -r requirements.txt 
13.Automatically it will download everything mentioned in requirements.txt and you can repeat this step for anything you want to install through this command
14.Create a new file setup.py which is entirely used for creating the packages
15.Inside setup.py file
   from setuptools import find_packages, setup

	setup(
	    name='DiamondPricePrediction',
	    Version='0.0.1',
	    author='AyazAnsari',
	    author_email="ayaz.ansari890@gmail.com",
	    install_requires=['pandas','sklearn'],
	    packages=find_packages()
	    )
16.Add in requirements.txt
	pandas
	numpy
	flask
17.What we do is that we create a function in setup.py file so that it reads the file that needs to be installed from requirements.txt
	from setuptools import find_packages, setup
	from typing import List

	def get_requirements(file_path:str)->List[str]:
	    requirements=[]
	    with open(file_path) as file_obj:
	        requirements=file_obj.readlines()
	        requirements=[req.replace("\n","") for req in requirements]

	        return requirements

	setup(
	    name='DiamondPricePrediction',
	    Version='0.0.1',
	    author='AyazAnsari',
	    author_email="ayaz.ansari890@gmail.com",
	    install_requires=get_requirements('requirements.txt'),
	    packages=find_packages()
	    )	

18.Now create a source folder as src and create a file inside it as __init__.py because whenever we install any packages it will be installed inside this.
19.Now open the terminal and type python setup.py install to install all the packages inside the requirements file
20.Now we see everything insalled and a package name DiamondPricePrediction is created
-----------------------------
Delete the packages build, DiamondPricePrediction.., dist
*. Write -e . in the requiremnt.txt (it is not a package but to trigger the setup.py file)
	pandas
	numpy	
	flask
	-e .
*. Write HYPEN_E_DOT='-e.' in the setup.py file

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup(
    name='DiamondPricePrediction',
    Version='0.0.1',
    author='AyazAnsari',
    author_email="ayaz.ansari890@gmail.com",
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
    )

*. In the terminal write pip install -r requirements.txt
 Then we see again the packages are installed
-----------------------------------------------------

2. Git Setup

1.Install Git CLI
2.write git in visual studio terminal, just to check if it is installed
3.Open github and create a new repository and give any name to it and don't need to tick any of the option
4.Open vscode and write git init in the terminal
5.Create a README.md file in the vscode and write anything inside it, eg. ## Machine Learning Project
6.Along with this create .gitignore file where we write the file names whom we don't want to be uploaded on github repository
	# Environments
	venv/
7.like whenever we commit then those files will be ignored
8.Now write git add .
9.git commit -m "first commit"
10.We see that except venv all files got selected
11.git branch -M main
12.git remote add origin https://github.com/AyazAnsari890/1.DS_DiamondPricePrediction.git
13.git push -u origin main
14.Refresh your github then we see all the files are uploaded
-----------------
15.Click on Add file->Create a file
16.Give a name .gitignore
17.Select Python in Choose.gitignore template
18.Copy the entire thing (not need to create this new file cancel changes)
19.Paste this whole thing in venv of vscode
20.Again do, git add .
21.git commit -m "Second Commit"
22.git push -u origin main
23.Now we see that there are updated changes in the venv file of our repository
-------------------------------------------------------

3. Project Structure

There are many files and folders in our project so it is important to maintain a proper project directory.
1.Open vscode and create a folder, artifacts here we store datasets, pickle files and models and whatever we serialize
2.Create another folder and subfolder, notebooks->data (for EDA and feature engineering)
There are two pipelines one is training pipeline and the other is prediction pipeline
3.Create two different folders components and pipelines inside src folder and also create __init__.py files inside both the folders.
4.Inside component folder we create data_ingestion.py, data_transformation.py, model_trainer.py files.
5.Inside pieplines folder we create training_pipeline.py and prediction_pipeline.py files.
6.Also we create utils.py file inside src folder. for common functionalities required for the project like reading a datafile from databases, csv files and picke files.
7.For every project we logging capabilities and exception handling capabilities so we create logger.py and exception.py inside src folder.
8.Update the git command and refresh the github reporsitory, we see all the files are uploaded except the empty files.
---------------------------------------------------------------------

4. Project Logging and Exception Handling

1.Copy the project code of logger.py and exception.py file in yours vscode files.
---------------------------------------------------------

5.EDA, FE and Model Training

The dataset has 10 independent feature and 1 as dependent/output feature ie. price

(After opening the vscode open new terminal type, activate
then conda activate e:\Data_Science_Project\Diamond_Price_Prediction\venv)
1.Add gemstone csv file inside data folder of notebooks
2.Add EDA.jpynb and Model Training.jpynb in notebooks folder.
3.Open the terminal and install ipykernal, pip install ipykernel to run any cells of the jupyter notebook in vscode.
4.Now run the cells of the code ie. of EDA.jpynb file.
5.Go to requirements.txt and add seaborn and then open the terminal and write pip install -r requirements.txt
6.For now you can delete the DiamondPricePrediction.. package created after installing the seaborn.
7.Now work with Model Training.jpynb file
8.We need to install sklearn, so go to requirements.txt and add scikit-learn and comment down -e . , as #-e .
9.Open terminal and write pip install -r requirements.txt
---------------------------------------------------------------------

6.Data Ingestion

Working on the reading of the dataset.

1.Open the components folder and work with data_ingestion.py file
2.Now we work with pipeline folder with training_pipeline.py file
3.Run your code written in training_pipeline.py, open terminal, python src/pipelines/training_pipeline.py
4.We see the path -> artifacts\train.csv artifacts\test.csv
5.Therefore we are able to successfully perform data ingestion and perform train and test split and save it into seperate file.
6.Also we are able to see the files created in the artifacts folder and the log files created.
7.We commit our code into the github
8.git add .
9.git commit -m "Data Ingestion"
10.git push -u origin main
-----------------------------------------------------------------------------

7.Data Transformation

Feature Engineering, Feature Scaling, Handling Missing Values
1.We take our ordinal and numerical data seperately and then we apply pipeline to handle missing values and categorical variables then we combine that particular 
  pipeline and create in the form of a pickle file.
2.Also we divide our train and test data and we work with data_transformation.py file.
3.Also use utils.py file to create all generic functionalities.
4.Now go to training_pipeline.py file and we initialize the data_transformation here and run our code. >python src/pipelines/training_pipeline.py
-----------------------------------------------------------------------------------

8.Model Training

We perform different model training on our dataset.
1.We open components folder and work with model_trainer.py file
2.We also work with utils.py file for creating model evalulation (in utils b'coz it is generic function)
3.Go to training_pipeline.py file and call the ModelTrainer method and then run your code.
4.We get to see that the Random Forest is the best model for this dataset.
---------------------------------------------------------------------------------------------

9.Prediction Pipeline

We create a front end GUI where we can give some value and get the price of the diamond.
1.Open Pipelines and work with prediction_pipeline.py
2.Open utils.py file and create a method for reading pickle file
3.Create custom variables for user input in prediction_pipeline.py file.
4.Close all the files and we need to use flask, first create application.py file and then along with we need create folder templates where we have html files. 
 create index.html file and form.html and work with these three files.
5.Now open terminal and run> python application.py



    

  
