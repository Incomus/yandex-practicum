## Table Of Content

- [Yandex Music Study](#yandex-music-study) - Basic Python
- [Borrower Reliability Research](#borrower-reliability-research) - Data Preprocessing
- [Research of Advertisements for the Sale of Apartments](#research-of-advertisements-for-the-sale-of-apartments) - Exploratory Data Analysis
- [Cellular Operator Tariffs Analysis](#cellular-operator-tariffs-analysis) - Statistical data analysis
- [Researching Historical Video Game Data](#Researching-Historical-Video-Game-Data) - Summary project 1
- [Introduction to Machine Learning](#Introduction-to-Machine-Learning)
- [Customer Churn Prediction](#Customer-Churn-Prediction) - Teacher-student model
- [Oil Well Location Selection](#Oil-Well-Location-Selection) - Machine learning in business


# [Yandex Music Study](https://github.com/Incomus/yandex-practicum/blob/main/5.%20Basic%20Python/big-city-music.ipynb)
## Basic Python

**Purpose of the study**: Test three hypotheses:
1. User activity depends on the day of the week, with differences between Moscow and St. Petersburg.
2. On Monday mornings and Friday evenings, different genres prevail in Moscow and St. Petersburg.
3. Moscow and St. Petersburg prefer different genres; Moscow prefers pop, and St. Petersburg prefers Russian rap.

## Data Overview
- **Dataset**: 65079 entries, 7 columns (user_id, track, artist, genre, city, time, day)
- **Sample Data**:
  | user_id | track                   | artist           | genre  | city             | time     | day       |
  |---------|-------------------------|------------------|--------|------------------|----------|-----------|
  | FFB692EC| Kamigata To Boots       | The Mass Missile | rock   | Saint-Petersburg | 20:28:33 | Wednesday |
  | 55204538| Delayed Because of Accident | Andreas Rönnberg | rock   | Moscow           | 14:07:09 | Friday    |
  | 20EC38  | Funiculì funiculà       | Mario Lanza      | pop    | Saint-Petersburg | 20:58:07 | Wednesday |
  | A3DD03C9| Dragons in the Sunset   | Fire + Ice       | folk   | Saint-Petersburg | 08:37:09 | Monday    |
  | E2DC1FAE| Soul People             | Space Echo       | dance  | Moscow           | 08:34:34 | Monday    |

- **Issues**: Mixed case, missing values, duplicates

## Data Preprocessing
- Renamed columns for consistency
- Filled missing values in 'track', 'artist', 'genre' with 'unknown'
- Removed duplicates

## Hypotheses Testing

### 1. User Activity
- **Hypothesis**: User activity varies by day and city.
- **Result**: Confirmed.
  - **Moscow**: Peak on Monday (15740) and Friday (15945), dip on Wednesday (11056)
  - **St. Petersburg**: Peak on Wednesday (7003), lower on Monday (5614) and Friday (5895)

### 2. Genre Preferences by Day and City
- **Hypothesis**: Different genres dominate on Monday mornings and Friday evenings in each city.
- **Result**: Partially confirmed.
  - **Monday Morning (7:00-11:00)**
    - **Moscow**: Top genres - pop (781), dance (549), electronic (480)
    - **St. Petersburg**: Top genres - pop (218), dance (182), rock (162)
  - **Friday Evening (17:00-23:00)**
    - **Moscow**: Top genres - pop (713), rock (517), dance (495)
    - **St. Petersburg**: Top genres - pop (256), electronic (216), rock (216)

### 3. Overall Genre Preferences
- **Hypothesis**: Moscow prefers pop, St. Petersburg prefers rap.
- **Result**: Not confirmed. 
  - **Moscow**: Top genres - pop (5892), dance (4435), rock (3965)
  - **St. Petersburg**: Top genres - pop (2431), dance (1932), rock (1879)

## Conclusion
- **First Hypothesis**: Confirmed - different user activity patterns by day and city.
- **Second Hypothesis**: Partially confirmed - minor genre differences on specific days.
- **Third Hypothesis**: Not confirmed - similar genre preferences in both cities.


# [Borrower Reliability Research](https://github.com/Incomus/yandex-practicum/blob/main/6.%20Data%20preprocessing/prep.ipynb)
## Data Preprocessing


## Overview
This project analyzes the reliability of borrowers based on various factors such as number of children, marital status, income level, and loan purpose.

## Data Overview
### Sample Data
Here are some examples of the dataset:

| children | days_employed | dob_years | education            | family_status     | gender | income_type | debt | total_income | purpose                            |
|----------|----------------|-----------|----------------------|-------------------|--------|-------------|------|--------------|------------------------------------|
| 1        | -8437.673028   | 42        | высшее               | женат / замужем   | F      | сотрудник   | 0    | 253875       | покупка жилья                     |
| 1        | -4024.803754   | 36        | среднее              | женат / замужем   | F      | сотрудник   | 0    | 112080       | приобретение автомобиля           |
| 0        | -5623.422610   | 33        | Среднее              | женат / замужем   | M      | сотрудник   | 0    | 145885       | покупка жилья                     |
| 3        | -4124.747207   | 32        | среднее              | женат / замужем   | M      | сотрудник   | 0    | 267628       | дополнительное образование        |
| 0        | 340266.072047  | 53        | среднее              | гражданский брак  | F      | пенсионер   | 0    | 158616       | сыграть свадьбу                   |

## Data Preprocessing
1. **Missing Values**: Filled missing values in 'total_income' and 'days_employed' based on 'income_type'.
2. **Anomalous Data**: Corrected negative values in 'days_employed' and removed invalid entries in 'children'.
3. **Data Type Conversion**: Converted 'total_income' to integer.
4. **Duplicates**: Processed and removed duplicate entries.
5. **Categorization**:
   - **Income Levels**:
     - `E`: 0–30000
     - `D`: 30001–50000
     - `C`: 50001–200000
     - `B`: 200001–1000000
     - `A`: 1000001 and above
   - **Loan Purposes**:
     - `операции с автомобилем`
     - `операции с недвижимостью`
     - `проведение свадьбы`
     - `получение образования`

## Data Exploration
1. **Children and Loan Repayment**:
   - Higher proportion of debtors among those with children.
   - Group without children has fewer debtors.

   | children | count | sum | mean   |
   |----------|-------|-----|--------|
   | 0        | 14149 | 1063| 7.51%  |
   | 1        | 4818  | 444 | 9.22%  |
   | 2        | 2055  | 194 | 9.44%  |
   | 3        | 330   | 27  | 8.18%  |
   | 4        | 41    | 4   | 9.76%  |
   | 5        | 9     | 0   | 0.00%  |

2. **Marital Status and Loan Repayment**:
   - Single and unmarried individuals have a higher share of debtors.
   - Previously married individuals have the smallest share of debtors.

   | family_status        | share of debtors |
   |----------------------|------------------|
   | Не женат / не замужем| 9.75%            |
   | женат / замужем      | 7.97%            |
   | вдовец / вдова       | 6.87%            |

3. **Income Level and Loan Repayment**:
   - Group C (medium income) has the highest proportion of debtors.
   - Group D (low income) has the smallest share of debtors.

   | total_income_category | count | sum | mean   |
   |-----------------------|-------|-----|--------|
   | C                     | 15992 | 1353| 8.46%  |
   | B                     | 5014  | 354 | 7.06%  |
   | D                     | 349   | 21  | 6.02%  |
   | A                     | 25    | 2   | 8.00%  |
   | E                     | 22    | 2   | 9.09%  |

4. **Loan Purpose and Repayment**:
   - Loans for cars and education have a higher share of debtors compared to weddings and real estate.

   | purpose_category        | share of debtors |
   |-------------------------|------------------|
   | операции с автомобилем  | 9.33%            |
   | получение образования   | 9.23%            |
   | проведение свадьбы      | 7.83%            |
   | операции с недвижимостью| 7.24%            |

## Conclusion
- **Children and Marital Status**: Borrowers with children and those who are not married are more likely to incur debt.
- **Income Level**: Medium earners (Group C) have the highest proportion of debtors.
- **Loan Purpose**: Loans for cars and education have the highest share of debtors.

Future analyses could include a joint study of the presence of children and marital status.

# [Research of Advertisements for the Sale of Apartments](https://github.com/Incomus/yandex-practicum/blob/main/7.%20Exploratory%20data%20analysis/real_estate_ads.ipynb)
## Exploratory Data Analysis

This project analyzes data from Yandex.Realty, an archive of apartment sale advertisements in St. Petersburg and nearby areas over several years. The objective is to determine market values, identify anomalies, and detect fraudulent activities for developing an automated tracking system.

## Data Description

- `airports_nearest`: Distance to the nearest airport in meters (m)
- `balcony`: Number of balconies
- `ceiling_height`: Ceiling height (m)
- `cityCenters_nearest`: Distance to the city center (m)
- `days_exposition`: Days the ad was active
- `first_day_exposition`: Publication date
- `floor`: Apartment floor
- `floors_total`: Total floors in the building
- `is_apartment`: Boolean indicating if it's an apartment
- `kitchen_area`: Kitchen area in square meters (m²)
- `last_price`: Price at removal from publication
- `living_area`: Living area in square meters (m²)
- `locality_name`: Name of the locality
- `open_plan`: Boolean indicating if it has an open plan
- `parks_around3000`: Number of parks within 3 km
- `parks_nearest`: Distance to the nearest park (m)
- `ponds_around3000`: Number of ponds within 3 km
- `ponds_nearest`: Distance to the nearest pond (m)
- `rooms`: Number of rooms
- `studio`: Boolean indicating if it's a studio
- `total_area`: Total area of the apartment in square meters (m²)
- `total_images`: Number of photos in the advertisement

## Exploratory Data Analysis

### Studying Object Parameters

- `total_area`:
  - Mean: 60.35 m²
  - Standard Deviation: 35.65 m²
  - Minimum: 12 m²
  - Maximum: 900 m²

- `living_area`:
  - Mean: 34.11 m²
  - Standard Deviation: 21.19 m²
  - Minimum: 2 m²
  - Maximum: 409.7 m²

- `kitchen_area`:
  - Mean: 10.57 m²
  - Standard Deviation: 5.91 m²
  - Minimum: 1.3 m²
  - Maximum: 112 m²

### Price Correlation

- `total_area` vs. `last_price` correlation: 0.654
- `living_area` vs. `last_price` correlation: 0.541
- `kitchen_area` vs. `last_price` correlation: 0.520
- `rooms` vs. `last_price` correlation: 0.363

### Top 10 Localities by Entries

- Saint Petersburg: 15,721 entries
- Murino: 556 entries
- Kudrovo: 472 entries
- Shushary: 440 entries
- Vsevolozhsk: 398 entries
- Pushkin: 369 entries
- Kolpino: 338 entries
- Pargolovo: 327 entries
- Gatchina: 307 entries
- Vyborg: 237 entries

### Average Price per Kilometer in Saint Petersburg

- Correlation of distance to city center vs. price: -0.250

## General Conclusion

The dataset includes extensive data on apartment sales, covering parameters such as area, price, and location. Analysis revealed significant correlations between apartment size and price, particularly in Saint Petersburg where proximity to the city center affects pricing dynamics. Insights gained from this study can aid in market predictions and anomaly detection for real estate transactions.

# [Cellular Operator Tariffs Analysis](https://github.com/Incomus/yandex-practicum/blob/main/8.%20Statistical%20data%20analysis/cellular_tarifs.ipynb)
## Statistical data analysis

You are an analyst working for a cellular operator. Customers are offered two tariff plans: "Smart" and "Ultra". To adjust the advertising budget, the commercial department wants to understand which tariff brings in more money.

## Description of Tariffs

### Tariff "Smart"
- **Monthly Fee:** 550 rubles
- **Includes:** 500 minutes of talk time, 50 messages, 15 GB of Internet traffic
- **Excess Charges:** 3 rubles per minute of conversation, 3 rubles per message, 200 rubles per GB of Internet traffic

### Tariff "Ultra"
- **Monthly Fee:** 1950 rubles
- **Includes:** 3000 minutes of talk time, 1000 messages, 30 GB of Internet traffic
- **Excess Charges:** 1 ruble per minute of conversation, 1 ruble per message, 150 rubles per GB of Internet traffic

## Data Overview

### Users Table
- Total users: 500
- Information available: user_id, age, city, registration date, tariff plan

### Calls Table
- Total calls recorded: 202,607
- Information available: call date, duration (minutes), user_id

### Messages Table
- Total messages sent: 123,036
- Information available: message date, user_id

### Internet Sessions Table
- Total sessions: 149,396
- Information available: session date, data used (MB), user_id

### Tariffs Table
- Information available for "Smart" and "Ultra" tariffs:
  - Included minutes, messages, and data (MB)
  - Excess charges for calls, messages, and data

## Data Analysis

- **7.6%** of clients terminated their contracts.
- Users on the "Ultra" tariff plan have longer average call durations compared to "Smart" users.
- Both tariffs show increasing trends in call duration and message usage throughout the year.
- Internet usage peaks vary with Smart users typically using 15–17 GB and Ultra users 19–21 GB.
- Hypothesis testing indicates significant differences in average revenue between "Ultra" and "Smart" tariff users (p-value < 0.05).

# [Researching Historical Video Game Data](https://github.com/Incomus/yandex-practicum/blob/main/10.%20Summary%20project%201/vg_research.ipynb)
## Summary project 1

- **Name**: The name of the game
- **Platform**: Platform
- **Year_of_Release**: Year of release
- **Genre**: Game genre
- **NA_sales**: Sales in North America (millions of copies sold)
- **EU_sales**: Sales in Europe (millions of copies sold)
- **JP_sales**: Sales in Japan (millions of copies sold)
- **Other_sales**: Sales in other countries (millions of copies sold)
- **Critic_Score**: Critics' score (maximum 100)
- **User_Score**: User rating (maximum 10)
- **Rating**: Rating from the ESRB (Entertainment Software Rating Board)

(Note: Data for 2016 may be incomplete.)

## Purpose of the Study

This study aims to analyze historical video game data to understand market trends and factors influencing game success. The objectives include:

- Explore the games represented in the dataset and their attributes.
- Identify patterns and correlations to determine the success metrics of video games.
- Test hypotheses regarding the impact of reviews, genres, and platforms on game sales.

## Brief Report

- Data was retrieved from the `games.csv` file, covering releases up to 2016. The dataset underwent preprocessing to handle missing values and ensure data consistency.
- A `sum_sales` column was added to quantify the global market performance of each game.
- Detailed exploratory data analysis was conducted, focusing on trends in game releases, platform sales, genre profitability, user profiles across different regions, and the impact of ESRB ratings.
- Hypotheses related to user and critic ratings' effects on game sales were tested using statistical methods.

## General Information

The dataset contains extensive information about video games released over several decades, including sales figures across different regions and critical reception metrics.

## Exploratory Data Analysis

### Game Releases by Year

The analysis revealed a decline in game releases post-2008, with a notable uptick in recent years, particularly for certain platforms.

### Sales by Platform for the Current Period (2013-2015)

Platforms such as PS4 and Xbox One showed significant growth during this period, despite an overall market decline.

### Impact of Reviews on Sales

Critic reviews showed a moderate correlation with game sales, while user reviews exhibited varied impacts across different genres and platforms.

### Distribution of Games by Genre

Action games dominated the market in terms of sheer number, while genres like platformers showed higher average sales per title.

### User Profiles

#### Platform Popularity by Region

PS4 and Xbox One led in North America and Europe, while Japan favored handheld consoles like the 3DS and PlayStation devices.

#### Genre Popularity by Region

North America and Europe showed a preference for action games, whereas Japan favored role-playing games and unique local genres.

### Impact of ESRB Rating

Games rated Mature (M) tended to sell better in North America and Europe, while Japanese sales were less influenced by ESRB ratings.

## Testing Hypotheses

- Average user ratings between Xbox One and PC platforms did not significantly differ (p-value: 0.14), suggesting similar user perceptions across these platforms.
- Average user ratings between Action and Sports genres differed significantly (p-value: 1.05e-27), indicating distinct user preferences and reception between these genres.

## General Conclusion

- The dataset reveals significant gaps in ratings data, particularly from the Japanese market, impacting the comprehensiveness of the analysis.
- Recent data (post-2013) provides more relevant insights into current market dynamics and platform performance.
- PS4 and Xbox One emerged as promising platforms, with action and shooter genres being the most profitable based on average sales.


# [Introduction to Machine Learning](https://github.com/Incomus/yandex-practicum/blob/main/11.%20Introduction%20to%20machine%20learning/users_behavior.ipynb)

This project explores the classification of suitable tariffs based on customer behavior data. The goal is to achieve a model accuracy of at least 75% on a test sample.

## Data Description

Each entry represents a user's behavior over a month, including:
- `calls`: Number of calls made
- `minutes`: Total call duration in minutes
- `messages`: Number of SMS messages sent
- `mb_used`: Internet traffic consumed in MB
- `is_ultra`: Binary indicator of the tariff used (0 - "Smart", 1 - "Ultra")

## Purpose of the Study

- Build and compare classification models
- Identify the model with the highest accuracy
- Validate model performance

## Brief Report

Data was sourced from the `users_behavior.csv` file. Three types of classification models were constructed using different hyperparameters. Model accuracies were assessed and hyperparameter dependencies analyzed.

### Data Overview

The dataset contains 3214 entries with 5 columns:
- `calls`: float64
- `minutes`: float64
- `messages`: float64
- `mb_used`: float64
- `is_ultra`: int64

## Sampling

The data was split into training, validation, and test sets using a 60-20-20 ratio.

## Model Creation and Testing

Models were built using:
- Decision Tree Classifier
- Random Forest Classifier
- Logistic Regression

The best performing model was a RandomForestClassifier with:
- `max_depth`: 7
- `n_estimators`: 60
- Accuracy: 81.03%

Other models included DecisionTreeClassifier (max accuracy: 80.72%) and LogisticRegression (max accuracy: 71.07%).

### Model Comparison

The highest accuracy was achieved by RandomForestClassifier, demonstrating the strongest predictive power for tariff classification.

## Conclusion

- DecisionTreeClassifier showed varying accuracy with different `max_depth` and `min_samples_leaf`.
- RandomForestClassifier's accuracy varied with `n_estimators` and `max_depth`.
- LogisticRegression consistently showed lower accuracy compared to tree-based models.


# [Customer Churn Prediction](https://github.com/Incomus/yandex-practicum/blob/main/12.%20Teacher-student%20model/Churn.ipynb)
## Teacher-student model

Clients are leaving Beta Bank each month, prompting the need to predict customer churn based on historical data. The goal is to build a model with the highest possible F1-measure, aiming for 0.59 on the test sample.

### Data Source
[Bank Customer Churn Modeling](https://www.kaggle.com/barelydedicated/bank-customer-churn-modeling)

### Features
- CreditScore: Credit rating
- Geography: Country of residence
- Gender: Gender
- Age: Age
- Tenure: Years as a bank client
- Balance: Account balance
- NumOfProducts: Number of bank products used
- HasCrCard: Availability of a credit card
- IsActiveMember: Client's activity status
- EstimatedSalary: Estimated salary

### Target Feature
- Exited: Whether the client has left the bank

### Purpose of the Study
- Build a model to predict customer churn
- Identify the model with the highest F1-measure
- Measure AUC-ROC for model comparison

### Brief Report
- Retrieved data from `Churn.csv`.
- Explored and preprocessed data, handling missing values and converting categorical features.
- Built three types of classification models (Decision Tree, Random Forest, Logistic Regression) and optimized them for F1-score.
- Corrected class imbalance using different methods (class_weight, upsample, downsample).
- Tested and validated the best performing model (Random Forest) achieving an F1-score of 0.616 on the test sample.
- Analyzed feature importance, identifying age as the most influential factor in predicting churn.

### Model Comparison
- **Decision Tree Classifier**: Achieved highest F1-score of 0.549 with max depth of 7.
- **Random Forest Classifier**: Outperformed other models with an F1-score of 0.616 using 30 estimators and a max depth of 10.
- **Logistic Regression**: Had the lowest F1-score of 0.294, indicating less suitability for this dataset.

### Class Imbalance Correction
- **Class Weight Balancing**: Increased F1-score to 0.617 by adjusting class weights.
- **Upsampling**: Enhanced F1-score to 0.611 by replicating minority class samples.
- **Downsampling**: Improved F1-score to 0.590 by reducing majority class samples.

### Conclusion
The RandomForestClassifier with balanced class weights provided the highest F1-score (0.616) and AUC-ROC (0.845) values, indicating its effectiveness in predicting customer churn. This model outperforms baseline and logistic regression models significantly, demonstrating its practical utility in reducing customer churn rates for Beta Bank.

### Additional Insights
- **Impact of Features**: Age, number of products used, and account balance were identified as the most influential factors in predicting churn.
- **Model Validation**: The model's performance on the test sample confirmed its robustness, achieving an F1-score of 0.620 and AUC-ROC of 0.845.
- **Business Recommendations**: Implement strategies based on predicted churn probabilities to proactively retain customers and optimize marketing efforts.


# [Oil Well Location Selection](https://github.com/Incomus/yandex-practicum/blob/main/13.%20Machine%20learning%20in%20business/well_loc.ipynb)
## Machine learning in business
We analyzed oil samples from three regions, each with 10,000 fields, measuring oil quality and reserve volume. The objective was to build a machine learning model to determine the most profitable region for oil mining and assess potential profits and risks using the Bootstrap technique.

## Steps to Select a Location:

- Search for deposits in each region and determine characteristic values.
- Build a model to estimate reserve volumes.
- Select deposits with the highest estimated values within budget constraints.
- Calculate total profit from selected fields.

## Data Description

Geological exploration data for three regions (`geo_data_0`, `geo_data_1`, `geo_data_2`):

- `id`: Unique identifier of the well
- `f0`, `f1`, `f2`: Point characteristics (features)
- `product`: Volume of reserves in the well (thousand barrels)

## Purpose of the Study

- Build models to forecast well reserve volumes in each region.
- Compare regions based on profitability and risk.
- Apply Bootstrap technique to assess risks and profitability.

## Brief Report

Data was obtained from three CSV files for the three regions (`geo_data_0.csv` to `geo_data_2.csv`).

- Three linear regression models were built for each region, and predictions were obtained for validation samples.
- The Bootstrap technique was applied to calculate average profits, confidence intervals, and risk of losses, proposing an optimal region.

## Data Overview

Data overview for each region:

- `geo_data_0`:
  - Number of records: 100,000
  - Columns: `id`, `f0`, `f1`, `f2`, `product`
  - Memory usage: 3.8 MB

- `geo_data_1`:
  - Number of records: 100,000
  - Columns: `id`, `f0`, `f1`, `f2`, `product`
  - Memory usage: 3.8 MB

- `geo_data_2`:
  - Number of records: 100,000
  - Columns: `id`, `f0`, `f1`, `f2`, `product`
  - Memory usage: 3.8 MB

## Model Creation and Testing

Since linear regression with three parameters is used, a third-order polynomial was applied. Each dataset (`geo_data_0`, `geo_data_1`, `geo_data_2`) was processed individually using the following steps:

- Data preprocessing involved removing the `id` column as it doesn't contribute to the model.
- Polynomial features were generated for training and validation.
- Linear regression models were trained and tested.
- Performance metrics including R-squared score, average product volume, and root-mean-square error (RMSE) were computed for each region.

|         | `geo_data_0` | `geo_data_1` | `geo_data_2` |
|---------|--------------|--------------|--------------|
| Score   | 0.285        | 1.000        | 0.253        |
| Product | 92.305       | 68.866       | 95.062       |
| RMSE    | 37.432       | 0.776        | 38.592       |

These metrics provide insights into the model's performance and the potential profitability of each region.


