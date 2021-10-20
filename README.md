# Overview & Goal
Classify whether a pt is obese
# Execute
## Run baseline model
### Run train and test
	python3 baseline.py
### To get val result
	python3 eval.py	
## Run SVM + TFIDF model
### Run train and test
	python3 nb_svm.py
### To get val result
	ipython -c "%run eval_svm.ipynb"
## run SVM + Word2vec model
### Run train and test
	ipython -c "%run word2vec.ipynb"
### To get val result
	python3 eval_word2vec.py
## Run SVM + doc2vec model
### Run train and test
	ipython -c "%run doc2vec.ipynb"
### To get val result
	ipython -c "%run eval_doc2vec.ipynb"
## Run SVM + Glove model
### Run train and test
	ipython -c "%run Glove.ipynb"
### To get val result
	ipython -c "%run eval_Glove.ipynb"
## Run LSTM
[LSTM](https://github.com/nomiaro/DigitalMedicine_Case1/blob/master/LSTM/README.md)
# Experiment result
Use textual train, Use intuitive test
## Baseline
![image](https://github.com/franktseng0718/DigitalMedicine_Case1/blob/master/baseline/baseline_result.PNG)
## SVM + TFIDF
![image](https://github.com/franktseng0718/DigitalMedicine_Case1/blob/master/nb_svm/SVM_result.PNG)
## SVM + word2vec
![image](https://github.com/franktseng0718/DigitalMedicine_Case1/blob/master/word2vec/Word2vec_result.PNG)
## SVM + doc2vec
![image](https://github.com/franktseng0718/DigitalMedicine_Case1/blob/master/doc2vec/doc2vec_result.PNG)
## SVM + Glove
![image](https://github.com/franktseng0718/DigitalMedicine_Case1/blob/master/Glove/Glove_result.PNG)
# Summary
### Top Kaggle public leaderboard score :
### LSTM
![image](https://github.com/nomiaro/DigitalMedicine_Case1/blob/master/LSTM/Experiment_Result.png)
