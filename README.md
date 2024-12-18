# mushroom_classification
Mid-term project. Ml-Zoomcamp 2024

## Description of the problem: 

The aim of the project is to build an train a Classifier that can distinguish between edible and poisonous mushrooms based on their physical characteristics. 
This could serve as a supportive tool for mushroom identification. While this classifier aims to provide accurate predictions, it should not replace expert knowledge or traditional mushroom identification methods. Always consult mycology experts and reliable guidebooks for mushroom foraging.


The dataset comes from the UCI Machine Learning Repository and includes descriptions of hypothetical samples of 23 species of gilled mushrooms in the Agaricus and Lepiota Family. Each species is identified as definitely edible or definitely poisonous. Species where the edibility is unknown or it is not recommended where also assigned to the poisonous class. 
The dataset contains 23 categorical features:

- cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s
- cap-surface: fibrous=f,grooves=g,scaly=y,smooth=s
- cap-color: brown=n,buff=b,cinnamon=c,gray=g,green=r,pink=p,purple=u,red=e,white=w,yellow=y
- bruises: bruises=t,no=f
- odor: almond=a,anise=l,creosote=c,fishy=y,foul=f,musty=m,none=n,pungent=p,spicy=s
- gill-attachment: attached=a,descending=d,free=f,notched=n
- gill-spacing: close=c,crowded=w,distant=d
- gill-size: broad=b,narrow=n
- gill-color: black=k,brown=n,buff=b,chocolate=h,gray=g, green=r,orange=o,pink=p,purple=u,red=e,white=w,yellow=y
- stalk-shape: enlarging=e,tapering=t
- stalk-root: bulbous=b,club=c,cup=u,equal=e,rhizomorphs=z,rooted=r,missing=?
- stalk-surface-above-ring: fibrous=f,scaly=y,silky=k,smooth=s
- stalk-surface-below-ring: fibrous=f,scaly=y,silky=k,smooth=s
- stalk-color-above-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y
- stalk-color-below-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y
- veil-type: partial=p,universal=u
- veil-color: brown=n,orange=o,white=w,yellow=y
- ring-number: none=n,one=o,two=t
- ring-type: cobwebby=c,evanescent=e,flaring=f,large=l,none=n,pendant=p,sheathing=s,zone=z
- spore-print-color: black=k,brown=n,buff=b,chocolate=h,green=r,orange=o,purple=u,white=w,yellow=y
- population: abundant=a,clustered=c,numerous=n,scattered=s,several=v,solitary=y
- habitat: grasses=g,leaves=l,meadows=m,paths=p,urban=u,waste=w,woods=d


## Run the project: 
You can clone the repository and run the notebooks in the conda environment specified in the environment.yml file. 
To create the environment run: 
```bash
conda env create -f environment.yml
```
The environment is called ml-zoomcamp-ubuntu. You can activate it by running:
```bash
conda activate ml-zoomcamp-ubuntu
``` 
The dataset is located in the data folder. You can also download it by running the first three commands of the notebook midterm_project.ipynb or download it from kaggle via the link: https://www.kaggle.com/datasets/uciml/mushroom-classification. 

## Running the Prediction Service

1. Navigate to the scripts directory:
```bash
cd scripts
```

2. Start the prediction service using Gunicorn:
```bash
gunicorn --bind 0.0.0.0:9696 predict:app
```

3. Open a new terminal window, activate the environment, and navigate to the scripts directory again:
```bash
conda activate ml-zoomcamp-ubuntu
cd scripts
```

4. Run the test script:
```bash
python predict_test.py
```

## Docker Deployment:
For the Docker deployment, we use Pipenv as it provides better compatibility with Docker containers and helps manage dependencies in a more isolated way.

1. Install Pipenv if you haven't already:
```bash
pip install pipenv
``` 
2. Activate the environment:
```bash
pipenv shell
```

3. Build the Docker image:
```bash
docker build -t mushroom-classifier .
```

4. Run the Docker container:
```bash
docker run -it --rm -p 9696:9696 mushroom-classifier
```

