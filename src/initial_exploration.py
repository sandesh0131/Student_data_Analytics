import pandas as pd


def dataset_shape(dataframe: pd.DataFrame) -> None:
    """Display the number of rows and columns."""

    rows, columns = dataframe.shape

    print("\n" + "=" * 60)
    print("DATASET SHAPE")
    print("=" * 60)
    print(f"Rows    : {rows}")
    print(f"Columns : {columns}")


def display_columns(dataframe: pd.DataFrame) -> None:
    """Display all column names."""

    print("\n" + "=" * 60)
    print("COLUMN NAMES")
    print("=" * 60)

    for index, column in enumerate(dataframe.columns, start=1):
        print(f"{index:02d}. {column}")


def check_data_types(dataframe: pd.DataFrame) -> None:
    """Display data types of each column."""

    print("\n" + "=" * 60)
    print("DATA TYPES")
    print("=" * 60)

    print(dataframe.dtypes)


def dataset_information(dataframe: pd.DataFrame) -> None:
    """Display dataset information."""

    print("\n" + "=" * 60)
    print("DATASET INFORMATION")
    print("=" * 60)

    dataframe.info()


def memory_usage(dataframe: pd.DataFrame) -> None:
    """Display memory usage."""

    memory_mb = dataframe.memory_usage(deep=True).sum() / (1024 ** 2)

    print("\n" + "=" * 60)
    print("MEMORY USAGE")
    print("=" * 60)

    print(f"Memory Used : {memory_mb:.2f} MB")


def summary_statistics(dataframe: pd.DataFrame) -> None:
    """Display summary statistics for numerical columns."""

    print("\n" + "=" * 60)
    print("SUMMARY STATISTICS")
    print("=" * 60)

    print(dataframe.describe().round(2))


def categorical_summary(dataframe: pd.DataFrame) -> None:
    """Display summary statistics for categorical columns."""

    print("\n" + "=" * 60)
    print("CATEGORICAL SUMMARY")
    print("=" * 60)

    print(dataframe.describe(include="object"))


def initial_observations(dataframe: pd.DataFrame) -> None:
    """Print practical observations about the dataset."""

    print("\n" + "=" * 60)
    print("INITIAL OBSERVATIONS")
    print("=" * 60)

    total_missing = dataframe.isna().sum().sum()
    duplicate_rows = dataframe.duplicated().sum()

    print(f"Total Missing Values : {total_missing}")
    print(f"Duplicate Rows       : {duplicate_rows}")
    print(f"Numeric Columns      : {len(dataframe.select_dtypes(include='number').columns)}")
    print(f"Categorical Columns  : {len(dataframe.select_dtypes(include='object').columns)}")