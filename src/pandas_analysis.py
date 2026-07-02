"""
pandas_analysis.py

Practical Pandas analysis for the Student Data Analytics System.
"""

import pandas as pd


def filter_high_cgpa_students(dataframe: pd.DataFrame) -> None:
    """
    Display students with CGPA >= 8.5.
    """

    high_cgpa = dataframe[dataframe["CGPA"] >= 8.5]

    print("\n" + "=" * 60)
    print("HIGH CGPA STUDENTS")
    print("=" * 60)

    print(
        high_cgpa[
            ["Student_ID", "Department", "CGPA", "Percentage"]
        ].head(10)
    )


def filter_low_attendance(dataframe: pd.DataFrame) -> None:
    """
    Display students having attendance below 75%.
    """

    low_attendance = dataframe[
        dataframe["Attendance_Percentage"] < 75
    ]

    print("\n" + "=" * 60)
    print("LOW ATTENDANCE STUDENTS")
    print("=" * 60)

    print(
        low_attendance[
            [
                "Student_ID",
                "Attendance_Percentage",
                "Department"
            ]
        ].head(10)
    )


def sort_by_percentage(dataframe: pd.DataFrame) -> None:
    """
    Sort students by Percentage.
    """

    sorted_students = dataframe.sort_values(
        by="Percentage",
        ascending=False
    )

    print("\n" + "=" * 60)
    print("TOP 10 STUDENTS")
    print("=" * 60)

    print(
        sorted_students[
            [
                "Student_ID",
                "Percentage",
                "CGPA"
            ]
        ].head(10)
    )


def department_summary(dataframe: pd.DataFrame) -> None:
    """
    Department-wise average performance.
    """

    summary = (
        dataframe
        .groupby("Department")
        .agg(
            Average_CGPA=("CGPA", "mean"),
            Average_Percentage=("Percentage", "mean"),
            Student_Count=("Student_ID", "count")
        )
        .round(2)
        .sort_values(
            by="Average_CGPA",
            ascending=False
        )
    )

    print("\n" + "=" * 60)
    print("DEPARTMENT SUMMARY")
    print("=" * 60)

    print(summary)


def attendance_summary(dataframe: pd.DataFrame) -> None:
    """
    Department-wise attendance.
    """

    attendance = (
        dataframe
        .groupby("Department")[
            "Attendance_Percentage"
        ]
        .mean()
        .round(2)
        .sort_values(ascending=False)
    )

    print("\n" + "=" * 60)
    print("ATTENDANCE SUMMARY")
    print("=" * 60)

    print(attendance)


def pivot_department_year(dataframe: pd.DataFrame) -> None:
    """
    Average CGPA by Department and Year.
    """

    pivot = pd.pivot_table(
        dataframe,
        values="CGPA",
        index="Department",
        columns="Year",
        aggfunc="mean"
    ).round(2)

    print("\n" + "=" * 60)
    print("PIVOT TABLE")
    print("=" * 60)

    print(pivot)


def scholarship_crosstab(dataframe: pd.DataFrame) -> None:
    """
    Scholarship distribution by Department.
    """

    cross = pd.crosstab(
        dataframe["Department"],
        dataframe["Scholarship"]
    )

    print("\n" + "=" * 60)
    print("SCHOLARSHIP CROSSTAB")
    print("=" * 60)

    print(cross)


def placement_query(dataframe: pd.DataFrame) -> None:
    """
    Students eligible for placement with good CGPA.
    """

    eligible = dataframe.query(
        "Placement_Eligible == 'Yes' and CGPA >= 7.5"
    )

    print("\n" + "=" * 60)
    print("PLACEMENT ELIGIBLE")
    print("=" * 60)

    print(
        eligible[
            [
                "Student_ID",
                "Department",
                "CGPA"
            ]
        ].head(10)
    )


def grade_value_counts(dataframe: pd.DataFrame) -> None:
    """
    Count students in each grade.
    """

    print("\n" + "=" * 60)
    print("GRADE DISTRIBUTION")
    print("=" * 60)

    print(dataframe["Grade"].value_counts())


def cgpa_rank(dataframe: pd.DataFrame) -> None:
    """
    Rank students based on CGPA.
    """

    ranked = dataframe.copy()

    ranked["CGPA_Rank"] = ranked["CGPA"].rank(
        ascending=False,
        method="dense"
    )

    print("\n" + "=" * 60)
    print("CGPA RANKING")
    print("=" * 60)

    print(
        ranked[
            [
                "Student_ID",
                "CGPA",
                "CGPA_Rank"
            ]
        ].head(10)
    )


def attendance_transform(dataframe: pd.DataFrame) -> None:
    """
    Compare attendance with department average.
    """

    transformed = dataframe.copy()

    transformed["Department_Average_Attendance"] = (
        transformed
        .groupby("Department")["Attendance_Percentage"]
        .transform("mean")
        .round(2)
    )

    print("\n" + "=" * 60)
    print("TRANSFORM EXAMPLE")
    print("=" * 60)

    print(
        transformed[
            [
                "Student_ID",
                "Department",
                "Attendance_Percentage",
                "Department_Average_Attendance"
            ]
        ].head()
    )


def merge_example(dataframe: pd.DataFrame) -> None:
    """
    Demonstrate merging with a small lookup table.
    """

    department_heads = pd.DataFrame({
        "Department": [
            "Computer",
            "IT",
            "Mechanical",
            "Civil",
            "Electronics"
        ],
        "Department_Head": [
            "Dr. Sharma",
            "Dr. Patel",
            "Dr. Rao",
            "Dr. Singh",
            "Dr. Mehta"
        ]
    })

    merged = pd.merge(
        dataframe,
        department_heads,
        on="Department",
        how="left"
    )

    print("\n" + "=" * 60)
    print("MERGE EXAMPLE")
    print("=" * 60)

    print(
        merged[
            [
                "Student_ID",
                "Department",
                "Department_Head"
            ]
        ].head(10)
    )