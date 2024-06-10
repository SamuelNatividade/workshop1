import pandas as pd


def load_excel(
    data_frame: pd.DataFrame, output_path: str, file_name: str
) -> str:
    """
    receber um dataframe e salvar como excel
    return "Arquivo salvo com sucesso.
    """
    data_frame.to_excel(f'{output_path}/{file_name}.xlsx', index=False)
    return 'Arquivo salvo com sucesso'
