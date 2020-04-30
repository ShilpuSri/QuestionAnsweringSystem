# QuestionAnsweringSystem
Question Answering System on Global Politics using NLP techniques
In this project, we implemented a Question Answering system using four distinct approaches enlisted below:

1. Closed Domain Question Answering using cdQA pipeline.
2. Latent Dirichlet Analysis
3. Hierarchical Dirichlet Processing
4. Unsupervised Modeling based on InferSent.

Please find the steps to run the code below:

1. Corpus Creation: Create your own corpus using Wikipedia pages on Politicians, Sports Politicians and Actor Politicians
 -> Text file "WikipediaPagesOn" contains names of the politicians (1600 politicians) on which we want the information. (You can update to add more such names)
 -> Run the file "Dataset Generation From Text File" to generate a "trainingDataset.csv" which contains a list of documents about all these Politicians.

2. We also have manually built the testing dataset "questions.csv" that has 400 queries corresponding to our corpus. Use it to query the models.


3. Running the models:
(i) cdQA: 
 -> Install the cdqa python library: pip install cdqa
 -> Run the file: cdQA.ipynb
 -> The final output with the answers gets stored in the file "qa_cdqa.csv"
 -> Accuracy = 0.93
 -> Time to run = approx 2.5 hours


(ii) LDA:
 -> Run the file LDAMallet.ipynb to obtain optimal number of topics as 120 based on Coherence Score
 -> Run the file QA_LDA.ipynb
 -> The final output with answers gets stored in the file "qa_lda.csv"
 -> Accuracy = 0.62
 -> Time to run = 5 mins

(iii) HDP:
  -> Run the file: QA_HDP.ipynb


(iv) Unsupervised Modeling using InferSent:
 -> Download InferSent, Facebook's Sentence Embedding from the github repository: https://github.com/facebookresearch/InferSent
 -> The /InferSent/encoder/ path should have files "infersent1.pkl", "infersent2.pkl"
 -> Download the GloVe Embedding, "glove.840B.300d.txt" and place it in the /InferSent/dataset/GloVe folder
 -> Provide these paths in the file "CreateSentenceEmbeddings.ipynb" in Cell #10 and #11.
 -> Run the file "CreateSentenceEmbeddings.ipynb"
 -> Run the file "QA_unsupervised.ipynb"
 -> The final output with the answers gets stored in the file "qa_unsupervised.csv"
 -> Accuracy = 0.77
 -> Time to run = 5 mins
 
