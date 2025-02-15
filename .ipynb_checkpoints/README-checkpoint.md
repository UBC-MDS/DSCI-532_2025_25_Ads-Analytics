# The Googleplay Apps - Ads Analytics Dashboard

## Authors

- Quanhua Huang
- Yeji Sohn  
- Lukman Lateef
- Ismail (Husain) Bhinderwala


## Motivation and Purpose of the Project

Advertisement companies face the challenge of sifting through large amounts of app data to determine which apps offer the best potential for advertising based on user engagement, ratings, and other metrics. If we could understand the factors that lead to higher sales and ratings, it may be possible to focus development resources to improve sales outcomes. 

To address this challenge, we propose building a data visualization app that allows the advertisement company to identify the most promising apps to target for ad placements. Solving this problem is crucial because effective ad targeting can significantly boost campaign performance and ROI. 

This dashboard will simplify decision-making by offering a clear, interactive interface to visualize key app metrics, helping the team identify high-potential apps quickly and make data-driven advertising decisions.

# Description of the data
We are using the [Google Play Store Apps](https://www.kaggle.com/datasets/lava18/google-play-store-apps) dataset, which includes features related to apps on the Google Play Store, such as app names, categories, ratings, and more. Our dataset consists of information on 9,660 apps, each with 9 different features. We aim to leverage these features to analyze how different factors impact ratings and installs, ultimately helping to make more informed advertising decisions.

We selected this dataset because it provides a comprehensive view of each app on the Google Play Store, offering valuable insights from various dimensions, including ratings, reviews, and categories. By visualizing the data, we hope to identify key factors that influence decision-making and determine which apps are more likely to benefit from improved ad placements.
We will focus on these nine features:

| **Features** | **Description** |
|-------------|----------------|
| `Category` | Category of the app belongs to |
| `Rating` | Overall user rating of the app |
| `Reviews` | Number of user reviews for the app |
| `Size` | Size of the app |
| `Installs` | Number of user downloads |
| `Type` | Paid or free |
| `Price` | Price for the app |
| `Content Rating` | Targeted age groups |
| `Genres` | Genre of the app |

In addition to the existing features, we will introduce new variables such as average_reviews (representing the average number of reviews for an app) and average_rating (indicating the app's average rating). These derived variables will provide deeper insights into the patterns, enabling us to draw more reliable conclusions about decision-making in advertising.

Before conducting any analysis, we will perform data wrangling and cleaning to handle missing values and ensure the dataset is ready for further exploration.



