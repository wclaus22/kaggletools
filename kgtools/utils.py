"""utils module"""


def class_weights(dataframe, column):
    """generate class weights from a dataframe and its resp. label column"""
    weights = {}
    for item in dataframe[column].unique():
        weight = (
            (1 / (len(dataframe[dataframe[column] == item]) / len(dataframe[column])))
            * 1
            / len(dataframe[column].unique())
        )
        weights[item] = weight
    return weights
