# Overview & Goal
Classify whether a pt is obese
# Execute
## run baseline model
	#run train and test
	python3 baseline.py
	#to get val result
	python3 eval.py	
## run SVM + TFIDF model
	#run train and test
	python3 nb_svm.py
	#to get val result
	ipython -c "%run eval_svm.ipynb"
## run SVM + Word2vec model
	#run train and test
	ipython -c "%run word2vec.ipynb"
	#to get val result
	python3 eval_word2vec.py
## run SVM + doc2vec model
	#run train and test
	ipython -c "%run doc2vec.ipynb"
	#to get val result
	ipython -c "%run eval_doc2vec.ipynb"
## run SVM + Glove model
	#run train and test
	ipython -c "%run Glove.ipynb"
	#to get val result
	ipython -c "%run eval_Glove.ipynb"
## run LSTM
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
Top Kaggle public leaderboard score
## LSTM
![image](https://github.com/nomiaro/DigitalMedicine_Case1/blob/master/LSTM/Experiment_Result.png)
