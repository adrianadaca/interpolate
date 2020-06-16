# interpolate
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
