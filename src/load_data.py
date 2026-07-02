import pandas as pd


def load_dataset(file_path: str) -> pd.DataFrame:
    """
    Load the student dataset from an Excel file.

    Parameters
    ----------
    file_path : str
        Path to the Excel file.

    Returns
    -------
    pd.DataFrame
        Loaded dataset.
    """

    try:
        dataframe = pd.read_excel(file_path)

        return dataframe

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    except Exception as error:
        raise Exception(
            f"Unable to load dataset.\n{error}"
        )