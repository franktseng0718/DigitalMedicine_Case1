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
![image](https://github.com/franktseng0718/DigitalMedicine_Case1/blob/master/baseline/baseline_result.PNG)
## svm + TFIDF
![image]()
## svm + word2vec
![image](https://github.com/franktseng0718/DigitalMedicine_Case1/blob/master/word2vec/Word2vec_result.PNG)
## svm + doc2vec
![image](https://github.com/franktseng0718/DigitalMedicine_Case1/blob/master/doc2vec/doc2vec_result.PNG)
## svm + Glove
![image](https://github.com/franktseng0718/DigitalMedicine_Case1/blob/master/Glove/Glove_result.PNG)
## LSTM
![image](https://github.com/nomiaro/DigitalMedicine_Case1/blob/master/LSTM/Experiment_Result.png)
