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
  <img src = https://content.presspage.com/uploads/2110/1920_potsvaccination.jpeg?10000>
</p> 

<p align="center">
  <img src = https://content.presspage.com/uploads/2110/1920_potsvaccination.jpeg?10000>
</p> 

## 2. Assigning Sentiment

Next, I used extensive lists of [positive](https://gist.github.com/mkulakowski2/4289437) words and [negative](https://gist.github.com/mkulakowski2/4289441) words to assign a score to each word (-1 for negative, 1 for positive, and 0 for neutral). I then added these scores together for each tweet to determine its 'sentiment_score.' If the score is positive, I'll labeled the tweet as "Positive"; if negative, as "Negative"; and if 0, as "Neutral."

<p align="center">
  <img src = https://content.presspage.com/uploads/2110/1920_potsvaccination.jpeg?10000>
</p> 

<p align="center">
  <img src = https://content.presspage.com/uploads/2110/1920_potsvaccination.jpeg?10000>
</p> 

## 3. Modeling

### Logistic Regression


### Naive Bayes


### Random Forest


### Support Vector Machine


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

## 5. Deployment

Below is the code for deploying the model and exporting the cleaned dataset.

The web app for this model can be found at ......
