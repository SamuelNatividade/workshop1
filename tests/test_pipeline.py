import pandas as pd 
from app.pipeline.transform import concat_data_frames

df_1 = pd.DataFrame({'col1': [1,2], 'col2':[3,4]})
df_2 = pd.DataFrame({'col1': [5,6], 'col2':[7,8]})

## estruturas de testes funcionam com arrange >> act >> assert.
def testar_a_concatenacao_da_lista_de_dataframe():
    dataframe_list = [df_1, df_2]
    df = concat_data_frames(dataframe_list)
    assert df.shape == (4,2)
