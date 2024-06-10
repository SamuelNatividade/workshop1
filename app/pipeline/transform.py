from typing import List

import pandas as pd


def concat_data_frames(data_frame_list: List) -> pd.DataFrame:
    """
    funcao para transformar uma lista de dataframes em um unico dataframe.
    """
    return pd.concat(data_frame_list)
