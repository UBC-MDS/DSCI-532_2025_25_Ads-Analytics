## Section 1: Motivation and Purpose

Our role: Data scientist consultancy firm

Target audience: Advertisement companies

Advertisement companies face the challenge of sifting through large amounts of app data to determine which apps offer the best potential for advertising based on user engagement, ratings, and other metrics. If we could understand the factors that lead to higher sales and ratings, it may be possible to focus development resources to improve sales outcomes. To address this challenge, we propose building a data visualization app that allows the advertisement company to identify the most promising apps to target for ad placements. Solving this problem is crucial because effective ad targeting can significantly boost campaign performance and ROI. This dashboard will simplify decision-making by offering a clear, interactive interface to visualize key app metrics, helping the team identify high-potential apps quickly and make data-driven advertising decisions.


## Section 2: Description of the data

We will be visualizing a dataset containing information about 10,000 Google Play Store apps. The dataset includes 13 columns, each representing different characteristics of the apps:

- App: Application name
- Category: Category the app belongs to
- Rating: Overall user rating of the app
- Reviews: Number of user reviews for the app
- Size: Size of the app
- Installs: Number of user downloads/installs
- Type: Paid or Free
- Price: Price of the app (if applicable)
- Content Rating: Age group the app is targeted at (e.g., Everyone, Teen, Mature 17+)
- Genres: Multiple genres the app belongs to
- Last Updated: Date when the app was last updated
- Current Ver: Current version of the app
- Android Ver: Minimum Android version required

The target audience for this project includes app developers, marketers, and business analysts who are interested in understanding the factors that contribute to the success of apps on the Google Play Store. By analyzing and visualizing this data, we aim to identify trends and insights that can help improve app development strategies, marketing efforts, and user engagement.


We plan to derive a new variable called User Engagement, which gives an idea of how engaged users are with the app, calculated as the number of reviews per installation..

## Section 3: Research questions and usage scenarios

**Research Question:**
1. app ranking/downloads based on reviews, by categories
2. Download to rating ratio
3. Correlation Between App Features and Downloads
4. categories based analysis for teens and everyone


Cameron is a marketing manager at a digital marketing agency, and she needs to optimize ad campaigns for her clients. She wants to explore app performance data in order to identify correlations between app features (like price, size, and genre) and downloads/ratings and compare performance across different app categories.

When Cameron logs on to our app analytics dashboard, she will see an overview of apps categorized by genre, size, price, and user ratings. She can filter the apps based on categories like "Games" or "Lifestyle" and sort them by download count and reviews. By comparing apps with different features, Cameron identifies that teen-focused apps tend to perform better when they are lightweight and free. Based on this information, Cameron adjusts her ad targeting strategy to focus on lightweight, free apps in the gaming and lifestyle categories.

Based on her findings from using our dashboard, Cameron hypothesizes that teens prefer apps that are both free and lightweight. She decides to refine her future campaigns by prioritizing these types of apps to improve the effectiveness of her ads.

## Section 4: App sketch & brief description
