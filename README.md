# Vaccine Sentiment Spectrum: Identifying Risks and Themes for Informed Public Health Action
#### By Rebekah McLaughlin

<p align="center">
  <img src = https://content.presspage.com/uploads/2110/1920_potsvaccination.jpeg?10000>
</p> 

## Overview

### Public Health Problem
The decision-making process behind individuals opting for or against vaccination can be very nuanced. However, the discourse surrounding the COVID-19 vaccines has remained polarized since their development, initial rollout, and up to the present day. 

While some individuals may have received the vaccine due to job requirements, for many, their decision hinged on **personal sentiments** towards vaccination.

Despite COVID-19 no longer being as acute a crisis in 2024 as it was during 2020-2021, it remains a leading cause of death in the United States and numerous other countries. Therefore, it is an ongoing priorety to protect those most vulnerable to the disease. As a major part of this effort, achieving herd immunity via individuals getting vaccinated is a continued top priority.

### Data-Driven Solution Effort

#### **The Dataset**

The [dataset](https://https://www.kaggle.com/datasets/gpreda/all-covid19-vaccines-tweets) is a collection of 228,207 rows, each containing a raw tweet's text, tweet ID, username, and other pertinent details. Every tweet in this dataset pertains to the COVID-19 vaccines. The tweets and associated information were collected by searching Twitter using the names of all the different COVID-19 vaccines. Then the dataset was subsequently donated to Kaggle in 2022.

#### **The Goal**

I will use this dataset to perform sentiment analysis on this collection of tweets. This will involve building several classification models. The model that demonstrates the highest accuracy in identifying the correct sentiment will be selected for deployment. The model will act as a tool to monitor changes in public sentiment towards the vaccine. My hope is that this tool will also facilitate public health initiatives aimed at continually encouraging vaccination against COVID-19.

## 1. Data Cleaning and Pre-processing

Although there was some missing data in the original dataframe, I only used one column, `'text'`.

Cleaning the text in this column required removing emojis, slang, URLs, usernames, and hashtags.

I then tokenized, removed stopwords, and lemmatized the text.

<p align="center">
  <img src = Images/corpusMCW.png>
</p> 

<p align="center">
  <img src = Images/corpuswordcloud.png>
</p> 

## 2. Assigning Sentiment

Next, I used extensive lists of [positive](https://gist.github.com/mkulakowski2/4289437) words and [negative](https://gist.github.com/mkulakowski2/4289441) words to assign a score to each word (-1 for negative, 1 for positive, and 0 for neutral). I then added these scores together for each tweet to determine its 'sentiment_score.' If the score is positive, I'll labeled the tweet as "Positive"; if negative, as "Negative"; and if 0, as "Neutral."

#### Most Common Positive Words
<p align="center">
  <img src = Images/positivewordcounts.png>
</p> 

<p align="center">
  <img src = Images/positivewordcloud.png>
</p> 

#### Most Common Negative Words
<p align="center">
  <img src = Images/negativewordcounts.png>
</p> 

<p align="center">
  <img src = Images/negativewordcloud.png>
</p> 

#### Most Common Neutral Words
<p align="center">
  <img src = Images/neutralwordcounts.png>
</p> 

<p align="center">
  <img src = Images/neutralwordcloud.png>
</p> 

## 3. Modeling

After thorough hyperparametric tuning, the four models I made and tested had the following results:

### Logistic Regression

<p align="center">
  <img src = Images/lorgregcm.png>
</p> 

#### **Logistic Regression Evaluation**

After hyperparameter tuning, my logistic regression model achieved an accuracy score of 0.96, with scores of 0.92 or higher across all metrics.

The model performed much better at distinguishing between 'Positive' and 'Negative' sentiments than between 'Neutral' and others.

### Naive Bayes

<p align="center">
  <img src = Images/naivebayescm.png>
</p> 

#### **Naive Bayes Evaluation**

After hyperparameter tuning, the Naive Bayes model did not perform as well as the Logistic Regression model. The maximum accuracy achieved by Naive Bayes was 0.79. This model performed significantly worse at misclassifying tweets as either 'Positive' or 'Negative'.

### Random Forest

<p align="center">
  <img src = Images/randomforestcm.png>
</p> 

#### **Random Forest Evaluation**

Hyperparameter tuning had minimal impact on the performance metrics of my Random Forest models. It did outperform Naive Bayes, but it only achieved an accuracy of 0.88. Logistic regression remains the front-runner far.

### Support Vector Machine

<p align="center">
  <img src = Images/svmcm.png>
</p> 

#### **SVM Evaluation**

The hyperparametric tuned SVM model performed the best at classifying the sentiment of the tweets, with an accuracy score of 0.98. 

Across the board, all metrics are 0.97 or higher!

## 4. Results

**Support Vector Machine** emerges as the best model, achieving an accuracy score of 0.98!

It's worth noting that there are alternative ways I could have chosen to pre-process the twitter text, particularly the way I treated 'Neutral' tweets. In sentiment analysis projects, data professionals often exclude neutral tweets to simplify the task for models. However, I made a deliberate choice not to do so, and there are two main reasons behind this decision:

1. A significant portion of the dataset was made up of neutral tweets, accounting for over half of the data. By excluding them, I would have disregarded a substantial amount of valuable data.

2. Many 'Neutral' tweets originated from news sources. Given Twitter's role as an information dissemination platform, this trend is likely to continue in the future. Therefore, keeping them seemed like they would help the model generalize better.

I also did not attempt to balance the target and chose to instead see how models would handle the imbalanced target. However, most of the models I used still managed to perform well at classifying 'Positive', 'Negative', and 'Neutral.'

Last assessments of model results:
- Logistic Regression, the initial model I employed, emerged as the runner-up with an accuracy score of 0.96.
- Naive Bayes performed the poorest in classifying all sentiments of tweets.
- I anticipated Random Forest to perform better, given its status as an ensemble method known for handling class imbalance well. However, it struggled to differentiate between neutral and negative sentiments and neutral and positive sentiments.

## Repository Structure

```
├──.devcontainer
├── Data
├── Images
├── README.md
├── Vaccine_Sentiment_Analysis_for_Informed_Public_Health_Action.ipynb
└── Vaccine_Sentiment_Analysis_for_Informed_Public_Health_Action.pdf
```
