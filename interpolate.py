import pandas as pd
import numpy as np

def interpolate(df1_index, df2_index, df1_column):
    '''
    This function uses linear interpolation to project the column values from a DataFrame with larger time steps onto
    the timestamps of a second DataFrame with smaller time steps.
    This is useful for doing calculations with data collected simultaneously from different sources that have
    different and irregular data collection frequencies.
    The first input is the index of the DataFrame with the larger time steps. The second input is the index of the
    DataFrame with the smaller time steps. The last input is the column from the first DataFrame that you would like
    to project to the timestamps of the second DataFrame. The indices of the DataFrames must be set as the timestamps
    using DataFrame.set_index(pd.DatetimeIndex(DataFrame['timestamp_column_name']), inplace=True)
    Example input: df1_column_projected = interpolate(df1.index, df2.index, df1.column_name)
    The output is the specified column of the first DataFrame projected onto the timestamps of the second DataFrame.
    '''
    
    df2_column_length = np.size(df2_index)
    df1_column_projected = np.zeros(df2_column_length)

    for j in range(0, df2_column_length):

        index1 = np.where(df1_index <= df2_index[j])
        index2 = np.where(df1_index >= df2_index[j])

        if any(map(len, index1)) and any(map(len, index2)):
            index1 = np.where(df1_index <= df2_index[j])[0][-1]
            index2 = np.where(df1_index >= df2_index[j])[0][0]
            if index1 == index2:
                df1_column_projected[j] = df1_column[index1]
            else:
                df1_column_projected[j] = (df2_index[j] - df1_index[index1]) * \
                                        (df1_column[index2] - df1_column[index1]) / \
                                        (df1_index[index2] - df1_index[index1]) + \
                                        df1_column[index1]
        else:
            df1_column_projected[j] = 0

    return df1_column_projected
