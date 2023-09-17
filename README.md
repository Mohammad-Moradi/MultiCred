# MultiCred
This project implements the "Multilevel User Credibility Assessment in Social Networks" article provided by the authors. All the packages used are placed in the requirements.txt file, and you can install them using the following command: <br>
&nbsp; &nbsp; &nbsp; &nbsp; `pip install -r requirements.txt` <br>
The dataset used is located in the `Labeled Data` directory. This dataset has been created from the original dataset after preprocessing. The list of features used is placed in the `Config.json` file. By running the `Data_Preprocessing.py` file on the original dataset, all the features specified in the Config file are extracted. You can extract your desired features by modifying this file.<br>

The `non_textual_features_vectorizer.ipynb` file transforms all the numerical features of user-profiles and their tweets into vectors and saves them in the `Non textual features` directory. The `non_textual_features_embedding.ipynb` file creates embeddings for numerical features for each user and places them in the `Non textual features` directory.<br>

The `mention_embedding.ipynb` file extracts mention text embeddings using sentiment analysis and save them in the `Textual features\Mentions` directory. `The tweet_embedding.ipynb` file transforms tweet texts into vectors using the BERT model and places them in the `Textual features\Tweets` directory.<br>

The `autoencoder.ipynb` file trains an autoencoder using tweet embeddings for dimensionality reduction in the next step. The trained autoencoder model is saved in the `Textual features\Tweets` directory. Then, the `tweet_text_autoencoder_embedding.ipynb` file calculates the final embeddings for tweets and places them in the `Textual features\Tweets` directory. <br>

Finally, the `classifier_model.ipynb` file creates the final model by reading the embedding file of textual and non-textual features. If the model is trained multiple times, the results are saved in the `Classifier Results` directory. <br>
