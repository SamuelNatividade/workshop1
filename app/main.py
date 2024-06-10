from pipeline.extract import extract_from_excel
from pipeline.load import load_excel
from pipeline.transform import concat_data_frames

if __name__ == '__main__':
    # extract
    listas_de_dataframes = extract_from_excel(
        path='/Users/samuelnatividade/Desktop/Projetos/workshop1/data/input'
    )
    # transform
    df_concat = concat_data_frames(listas_de_dataframes)
    # load
    load_excel(
        data_frame=df_concat,
        output_path='/Users/samuelnatividade/Desktop/Projetos/workshop1/data/output',
        file_name='output_data',
    )
