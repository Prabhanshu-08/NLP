# NLP-Guide

![ezgif com-gif-maker](https://user-images.githubusercontent.com/88246010/224085559-6d44c273-813b-4ff9-8bd7-c24a452ae495.gif)

It a NLP project able to identify the tweets of a disaster in happening. It is trained on over 7000+ tweets and can achieve an validation accuracy of 83%. More details about NLP can be found in this [blog](https://medium.com/@prabhanshugupta008/from-text-to-insights-a-beginners-guide-to-nlp-applications-2bcd2b1b38e6).

**Data Source**

[KAGGLE](https://www.kaggle.com/competitions/nlp-getting-started)

**Motivation**

Twitter has become an important communication channel in times of emergency. The availability of smartphones enables people to announce an emergency they’re observing in real-time. Because of this, more agencies are interested in programatically monitoring Twitter (i.e. disaster relief organizations and news agencies). This project is aimed to classify such tweets and alert the authorities so that help can be provided to people in need on time.

**Built with**

1. Matplotlib
2. Pandas
3. Numpy
4. Seaborn
5. Tensorflow
6. Keras

**Usage**

* Before the following steps make sure you have [git](https://git-scm.com/download), [Anaconda](https://www.anaconda.com/) or [miniconda](https://docs.conda.io/en/latest/miniconda.html) installed on your system

* Clone the complete project with git clone https://github.com/Prabhanshu-08/NLP.git or you can just download the code and unzip it

* Once the project is cloned, open anaconda prompt in the directory where the project was cloned and paste the following block

```
conda create -n disaster_tweet python=3.9.6
pip install -r requirements.txt
conda activate disaster_tweet 
```

* After creating an environment go to this [drive](https://drive.google.com/drive/folders/1-0ha1sOyvCcklajy-Nt7_xedsByqJQvG?usp=share_link) link and download 'Disaster_tweet' file and place it in same 'disaster_tweet' folder. This was done to copy the model which will do the predictions. Since this model was large in size it could not be hosted in github.

* And finally run the project with
```python app.py```

* Open the localhost url provided after running app.py and now you can use the project locally in your web browser.

**DEMO**

* Home Page
![image](https://user-images.githubusercontent.com/88246010/224098519-d7ac9c5f-45cf-49ba-b3e6-0b9c2dca1d8d.png)

* If it is just a normal tweet
![image](https://user-images.githubusercontent.com/88246010/224098852-a367c2d6-012b-4b6c-8415-a34e4e7a9389.png)

* If it is tweet of a disaster in happpening
![image](https://user-images.githubusercontent.com/88246010/224099041-4fef6d52-8e84-4080-a33e-fc856bd2dae7.png)

**Further Improvements**
1. Contact details of responsible person can be made visible on prediction page in case of a tweet which is about a disaster in happening
2. More data can be added in training to further increase the accuracy of model.

**Contact**

If you have any doubt or want to contribute feel free to email me or hit me up on [LinkedIn](https://www.linkedin.com/in/prabhanshu-gupta-71248118a/
)

