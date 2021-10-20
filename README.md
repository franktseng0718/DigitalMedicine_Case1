# Overview & Goal
Classify whether a pt is obese
# Execute
## run baseline model
	python3 baseline.py
	#run train and test
	python3 eval.py
	#to get val result
## run svm + TFIDF model
	python3 nb_svm.py
	#run train and test
	ipython -c "%run eval_svm.ipynb"
	#to get val result
## run svm + Word2vec model
	ipython -c "%run word2vec.ipynb"
	#run train and test
	python3 eval_word2vec.py
	#to get val result
## run svm + doc2vec model
	ipython -c "%run doc2vec.ipynb"
	#run train and test
	ipython -c "%run eval_doc2vec.ipynb"
	#to get val result
## run svm + Glove model
	ipython -c "%run Glove.ipynb"
	#run train and test
	ipython -c "%run eval_Glove.ipynb"
	#to get val result
## run LSTM
[LSTM](https://github.com/nomiaro/DigitalMedicine_Case1/blob/master/LSTM/README.md)
# Experiment result
## Baseline
## svm + TFIDF
## svm + word2vec
## svm + doc2vec
## svm + Glove
## LSTM
![image](https://github.com/nomiaro/DigitalMedicine_Case1/blob/master/LSTM/Experiment_Result.png)
