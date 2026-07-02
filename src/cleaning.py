import pandas as pd


def handle_missing_values(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values using practical strategies.
    """

    df = dataframe.copy()

    numeric_columns = df.select_dtypes(include="number").columns
    categorical_columns = df.select_dtypes(include="object").columns

    # Fill numeric columns with median
    for column in numeric_columns:
        if df[column].isnull().sum() > 0:
            df[column] = df[column].fillna(df[column].median())

    # Fill categorical columns with mode
    for column in categorical_columns:
        if df[column].isnull().sum() > 0:
            mode_value = df[column].mode()

            if not mode_value.empty:
                df[column] = df[column].fillna(mode_value[0])

    return df


def remove_duplicate_records(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows.
    """

    before = len(dataframe)

    df = dataframe.drop_duplicates().copy()

    removed = before - len(df)

    print(f"\nDuplicate Records Removed : {removed}")

    return df


def standardize_column_names(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names.
    """

    df = dataframe.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    return df


def clean_string_columns(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Remove unwanted spaces from text columns.
    """

    df = dataframe.copy()

    object_columns = df.select_dtypes(include="object").columns

    for column in object_columns:
        df[column] = (
            df[column]
            .astype(str)
            .str.strip()
        )

    return df


def standardize_text_values(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize selected categorical values.
    """

    df = dataframe.copy()

    replacements = {
        "Gender": {
            "male": "Male",
            "MALE": "Male",
            "female": "Female",
            "FEMALE": "Female"
        },

        "Scholarship": {
            "yes": "Yes",
            "YES": "Yes",
            "no": "No",
            "NO": "No"
        },

        "Hosteller": {
            "yes": "Yes",
            "YES": "Yes",
            "no": "No",
            "NO": "No"
        },

        "Placement_Eligible": {
            "yes": "Yes",
            "YES": "Yes",
            "no": "No",
            "NO": "No"
        }
    }

    for column, mapping in replacements.items():
        if column in df.columns:
            df[column] = df[column].replace(mapping)

    return df


def convert_data_types(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Convert columns to appropriate data types where possible.
    """

    df = dataframe.copy()

    numeric_columns = [
        "Age",
        "Attendance_Percentage",
        "Assignment_Marks",
        "Internal_Marks",
        "Midterm_Marks",
        "Final_Exam_Marks",
        "Project_Marks",
        "Practical_Marks",
        "Sports_Marks",
        "Library_Visits",
        "Study_Hours_Per_Day",
        "Internet_Usage_Hours",
        "Family_Income",
        "CGPA",
        "Percentage",
        "Backlogs"
    ]

    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    return df


def export_cleaned_dataset(
    dataframe: pd.DataFrame,
    output_path: str
) -> None:
    """
    Export cleaned dataset.
    """

    dataframe.to_excel(
        output_path,
        index=False
    )

    print(f"\nCleaned dataset saved to: {output_path}")