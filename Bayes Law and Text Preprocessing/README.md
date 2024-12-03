## Project Overview

This project focuses on the implementation and use of **Bayes’ Theorem** in text classification. The aim is to preprocess text data and use **Naive Bayes** classification for categorizing books based on their descriptions.

## Key Components of the Project:

### 1. Bayes’ Theorem
Bayes' Theorem is used to calculate the probability of a given hypothesis based on prior knowledge and observed data. The theorem is essential for tasks like classification and prediction.
   - The formula used is:
   \[
   P(c|x) = \frac{P(x|c)P(c)}{P(x)}
   \]
   where:
   - \(P(c|x)\): Posterior probability
   - \(P(x|c)\): Likelihood
   - \(P(c)\): Prior probability
   - \(P(x)\): Evidence

### 2. Text Preprocessing
Text preprocessing involves cleaning the data by removing punctuation, numbers, and unnecessary characters from the book descriptions.
   - Additionally, stemming and lemmatization techniques are used to ensure that words with similar roots are treated as the same during classification.

### 3. Book Classification
The dataset contains descriptions of books that belong to six categories: Novels, Short Stories, Sociology, Islamic Studies, Management, and Children's Literature.
   - The objective is to classify books into the correct category based on their descriptions using a Naive Bayes classifier.

## Project Phases:

### Phase 1: Data Preprocessing
   - Preprocess the text data using the `hazm` library for Persian text processing.
   - Remove irrelevant characters and words that do not contribute to classification.
   - Implement word tokenization and construct a Bag of Words (BoW) model for each book.

### Phase 2: Naive Bayes Classification
   - Use the preprocessed text data to apply **Naive Bayes** classification.
   - Train the classifier using the `books_train.csv` dataset and predict the categories for books in the `books_test.csv` dataset.
   - Implement additive smoothing to handle unseen words in the test data.

### Phase 3: Improving Accuracy
   - Apply stemming and lemmatization to improve classification accuracy.
   - Remove common stop words, which do not provide significant information for classification.

## Deliverables:
- **Preprocessed Text Data**: Text data after applying preprocessing techniques.
- **Naive Bayes Classifier**: Code for training and predicting book categories using the Naive Bayes algorithm.
- **Evaluation**: Test the accuracy of the classifier using test data.
- **Report**: Detailed documentation of the steps followed, including the classification results and any performance improvements.

This project is part of the **Probability and Statistics** course at the University of Tehran.