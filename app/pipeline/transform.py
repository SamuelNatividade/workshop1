import pandas as pd 
from typing import List

"""
funcao para transformar uma lista de dataframes em um unico dataframe
"""

def concat_data_frames(data_frame_list: List) -> pd.DataFrame:
    return pd.concat(data_frame_list)