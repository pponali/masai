# Handling Messy Data

    Now we have taken the raw data and started to explore it. We have seen that some missing values and duplicate values are present in the data. We will now handle these issues and make the data ready for analysis.

## Handling missing data

We have handled missing values by adding the median to age and mode to city.

## Handling duplicate data

We have handled duplicate values by dropping them.

## Encoding Data

### One hot encoding

    One hot encoding is used to convert categorical variables into a format that can be provided to machine learning algorithms to do a better job in prediction.

### Label encoding

    Label encoding is used to convert categorical variables into numerical values, which can be used by machine learning algorithms.

### One hot encoding vs Label encoding

    One hot encoding is used when the categorical variable is nominal, which means that there is no order or hierarchy among the categories. Label encoding is used when the categorical variable is ordinal, which means that there is an order or hierarchy among the categories.

    Example for One hot encoding: One hot encoding is used for the city column, as there is no order among the cities. Label encoding is used for the gender column, as there is an order among the genders.

    Example for Label encoding: Label encoding is used for the gender column, as there is an order among the

## Scaling

    Scaling is meant for bring the large values into machine understandble format.

### Min Max Scaling

    Min Max Scaling is used to scale the data to a fixed range, usually 0 to 1.

### Standard scaling

    Standard scaling is used to scale the data to have a mean of 0 and a standard deviation of 1.
