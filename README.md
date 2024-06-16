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
```
