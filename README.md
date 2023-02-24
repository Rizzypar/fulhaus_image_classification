# fulhaus_image_classification
Fulhaus Image Classification Model
DESCRIPTION:

The dataset provided consists of 3 classes. Based on this dataset, following instructions were attempted.

Build a classification model (Deep learning preferred). Build an API to access the model. The API should accept an image as input and return the predicted label (category) as output (Preferred frameworks based on Python). Create a Docker image of your code by following docker best practices. Implement CI/CD pipeline on Github Actions. Add a clear README file with instructions.

TOOLS USED:

Jupyter Notebooks

Pycharm

Docker

DATASET:

The dataset had three folders namely Bed, Sofa, and Chairs containing the respective images having varying pixel dimensions.

To accommodate that in the code for ease, I scripted a program that included changing the pixels from varying data to 128*128 dimensions each.

STEPS:

As the data given had class labels, supervised learning was opted thereby Convolution Neural Networks(CNN) was used. To test the model on real data we used an application using the Gradio library of python. Since the code running in my PC(Jupyter Notebook) worked accordingly with respect to the library installed locally. I containerized or dockerized the application so that anyone can access the code without the need to download the libraries in their system. We are pushing the models to github, for the version control, any new changes can be tracked, and used to enhance the model. CI/CD - hold

# Steps To Run The Project
Clone the project using:
git clone https://github.com/Rizzypar/fulhaus_image_classification.git

Navigate to the cloned folder run the docker build command as shown below:
$docker build . -f DOCKERFILE -t test

Next run the docker image created in the previous step using the below command:
$docker run -it -d --name test -p 7000:7000 --network=host test:latest

Once this runs you can check the logs of the currently running docker for the localhost link as shown below:
$docker logs -f test

# Alternative way to Run The Project
Clone the repository using:
git clone https://github.com/Rizzypar/fulhaus_image_classification.git

Install required libraies mentioned in the requirements.txt using:
pip install $library_name

Once all libraries are installed, run the below command to access the model:
python app.py
