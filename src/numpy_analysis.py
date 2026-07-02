"""
numpy_analysis.py

Practical NumPy analysis for the Student Data Analytics System.
"""

import numpy as np
import pandas as pd


def dataframe_to_numpy(dataframe: pd.DataFrame) -> np.ndarray:
    """
    Convert DataFrame to NumPy array.
    """

    try:
        return dataframe.to_numpy()

    except Exception as error:
        raise Exception(f"Error converting DataFrame to NumPy array: {error}")


def basic_statistics(dataframe: pd.DataFrame) -> None:
    """
    Display descriptive statistics for Percentage.
    """

    try:
        percentages = dataframe["Percentage"].to_numpy()

        print("\n" + "=" * 60)
        print("PERCENTAGE STATISTICS")
        print("=" * 60)

        print(f"Mean               : {np.mean(percentages):.2f}")
        print(f"Median             : {np.median(percentages):.2f}")
        print(f"Variance           : {np.var(percentages):.2f}")
        print(f"Standard Deviation : {np.std(percentages):.2f}")

        print("\nPercentiles")

        for percentile in [25, 50, 75, 90]:
            value = np.percentile(percentages, percentile)
            print(f"{percentile}% : {value:.2f}")

    except Exception as error:
        print(f"Error: {error}")


def array_slicing(dataframe: pd.DataFrame) -> None:
    """
    Demonstrate array slicing.
    """

    try:
        selected_columns = [
            "Student_ID",
            "Department",
            "CGPA",
            "Percentage"
        ]

        student_array = dataframe[selected_columns].to_numpy()

        print("\n" + "=" * 60)
        print("FIRST FIVE STUDENTS")
        print("=" * 60)

        print(student_array[:5])

    except Exception as error:
        print(f"Error: {error}")


def high_performers(dataframe: pd.DataFrame) -> None:
    """
    Display students having CGPA >= 8.5.
    """

    try:
        cgpa = dataframe["CGPA"].to_numpy()

        top_students = dataframe[cgpa >= 8.5]

        print("\n" + "=" * 60)
        print("HIGH PERFORMERS")
        print("=" * 60)

        print(
            top_students[
                [
                    "Student_ID",
                    "Department",
                    "CGPA",
                    "Percentage"
                ]
            ].head(10)
        )

    except Exception as error:
        print(f"Error: {error}")


def attendance_filter(dataframe: pd.DataFrame) -> None:
    """
    Students having attendance greater than or equal to 85%.
    """

    try:
        attendance = dataframe["Attendance_Percentage"].to_numpy()

        students = dataframe[attendance >= 85]

        print("\n" + "=" * 60)
        print("GOOD ATTENDANCE")
        print("=" * 60)

        print(
            students[
                [
                    "Student_ID",
                    "Attendance_Percentage",
                    "CGPA"
                ]
            ].head(10)
        )

    except Exception as error:
        print(f"Error: {error}")


def sort_percentages(dataframe: pd.DataFrame) -> None:
    """
    Sort Percentage values.
    """

    try:
        percentages = dataframe["Percentage"].to_numpy()

        sorted_percentages = np.sort(percentages)

        print("\n" + "=" * 60)
        print("SORTED PERCENTAGES")
        print("=" * 60)

        print("\nLowest Five")
        print(sorted_percentages[:5])

        print("\nHighest Five")
        print(sorted_percentages[-5:])

    except Exception as error:
        print(f"Error: {error}")


def random_sample(dataframe: pd.DataFrame, sample_size: int = 5) -> None:
    """
    Display random student records.
    """

    try:
        random_indices = np.random.choice(
            dataframe.index,
            size=sample_size,
            replace=False
        )

        print("\n" + "=" * 60)
        print("RANDOM SAMPLE")
        print("=" * 60)

        print(
            dataframe.loc[
                random_indices,
                [
                    "Student_ID",
                    "Department",
                    "CGPA",
                    "Percentage"
                ]
            ]
        )

    except Exception as error:
        print(f"Error: {error}")


def assignment_bonus(dataframe: pd.DataFrame) -> None:
    """
    Add 5 bonus marks using NumPy broadcasting.
    Maximum marks are capped at 100.
    """

    try:
        marks = dataframe["Assignment_Marks"].to_numpy()

        updated_marks = np.minimum(marks + 5, 100)

        print("\n" + "=" * 60)
        print("ASSIGNMENT BONUS")
        print("=" * 60)

        print("Before:")
        print(marks[:10])

        print("\nAfter:")
        print(updated_marks[:10])

    except Exception as error:
        print(f"Error: {error}")


def academic_average(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate average academic marks using vectorized operations.
    """

    try:
        academic_columns = [
            "Assignment_Marks",
            "Internal_Marks",
            "Midterm_Marks",
            "Final_Exam_Marks",
            "Project_Marks",
            "Practical_Marks"
        ]

        marks = dataframe[academic_columns].to_numpy()

        average = np.mean(
            marks,
            axis=1
        )

        dataframe["Academic_Average"] = np.round(average, 2)

        print("\n" + "=" * 60)
        print("ACADEMIC AVERAGE")
        print("=" * 60)

        print(
            dataframe[
                [
                    "Student_ID",
                    "Academic_Average"
                ]
            ].head()
        )

        return dataframe

    except Exception as error:
        print(f"Error: {error}")
        return dataframe


def percentile_analysis(dataframe: pd.DataFrame) -> None:
    """
    Display important percentile values for CGPA.
    """

    try:
        cgpa = dataframe["CGPA"].to_numpy()

        print("\n" + "=" * 60)
        print("CGPA PERCENTILES")
        print("=" * 60)

        for percentile in [10, 25, 50, 75, 90]:
            print(
                f"{percentile}% : "
                f"{np.percentile(cgpa, percentile):.2f}"
            )

    except Exception as error:
        print(f"Error: {error}")


def department_random_sample(dataframe: pd.DataFrame) -> None:
    """
    Display 10 random departments from the dataset.
    """

    try:
        departments = dataframe["Department"].to_numpy()

        sample = np.random.choice(
            departments,
            size=10,
            replace=False
        )

        print("\n" + "=" * 60)
        print("RANDOM DEPARTMENTS")
        print("=" * 60)

        print(sample)

    except Exception as error:
        print(f"Error: {error}")


def cgpa_distribution(dataframe: pd.DataFrame) -> None:
    """
    Display CGPA distribution information.
    """

    try:
        cgpa = dataframe["CGPA"].to_numpy()

        print("\n" + "=" * 60)
        print("CGPA DISTRIBUTION")
        print("=" * 60)

        print(f"Minimum CGPA : {np.min(cgpa):.2f}")
        print(f"Maximum CGPA : {np.max(cgpa):.2f}")
        print(f"Average CGPA : {np.mean(cgpa):.2f}")

    except Exception as error:
        print(f"Error: {error}")


def marks_statistics(dataframe: pd.DataFrame) -> None:
    """
    Display statistics for all academic marks.
    """

    try:
        columns = [
            "Assignment_Marks",
            "Internal_Marks",
            "Midterm_Marks",
            "Final_Exam_Marks",
            "Project_Marks",
            "Practical_Marks"
        ]

        marks = dataframe[columns].to_numpy()

        print("\n" + "=" * 60)
        print("ACADEMIC MARKS STATISTICS")
        print("=" * 60)

        print(f"Overall Mean      : {np.mean(marks):.2f}")
        print(f"Overall Median    : {np.median(marks):.2f}")
        print(f"Minimum Marks     : {np.min(marks):.2f}")
        print(f"Maximum Marks     : {np.max(marks):.2f}")
        print(f"Standard Deviation: {np.std(marks):.2f}")

    except Exception as error:
        print(f"Error: {error}")