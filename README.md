# 5. [Basic Python](https://github.com/Incomus/yandex-practicum/blob/main/5.%20Basic%20Python/big-city-music.ipynb)
## Yandex Music Study

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


# 
# 5. [Data preprocessing](https://github.com/Incomus/yandex-practicum/blob/main/6.%20Data%20preprocessing/prep.ipynb)
## Borrower Reliability Research


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
```
