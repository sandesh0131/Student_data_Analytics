"""
export_reports.py

Export analytical reports to Excel.
"""

import os
import pandas as pd


OUTPUT_FOLDER = "data"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def export_top_students(df: pd.DataFrame) -> None:
    """
    Export top 10 students based on Percentage.
    """

    top_students = (
        df.sort_values("Percentage", ascending=False)
        .head(10)
    )

    top_students.to_excel(
        os.path.join(OUTPUT_FOLDER, "top_students.xlsx"),
        index=False
    )

    print("✓ top_students.xlsx exported")


def export_placement_students(df: pd.DataFrame) -> None:
    """
    Export placement eligible students.
    """

    placement_students = df[
        df["Placement_Eligible"] == "Yes"
    ]

    placement_students.to_excel(
        os.path.join(
            OUTPUT_FOLDER,
            "placement_students.xlsx"
        ),
        index=False
    )

    print("✓ placement_students.xlsx exported")


def export_failed_students(df: pd.DataFrame) -> None:
    """
    Export students who failed.
    """

    failed_students = df[
        df["Result"] == "Fail"
    ]

    failed_students.to_excel(
        os.path.join(
            OUTPUT_FOLDER,
            "failed_students.xlsx"
        ),
        index=False
    )

    print("✓ failed_students.xlsx exported")


def export_department_summary(df: pd.DataFrame) -> None:
    """
    Export department summary.
    """

    summary = (
        df.groupby("Department")
        .agg(
            Students=("Student_ID", "count"),
            Average_CGPA=("CGPA", "mean"),
            Average_Percentage=("Percentage", "mean"),
            Average_Attendance=(
                "Attendance_Percentage",
                "mean"
            ),
            Placement_Eligible=(
                "Placement_Eligible",
                lambda x: (x == "Yes").sum()
            )
        )
        .round(2)
        .reset_index()
    )

    summary.to_excel(
        os.path.join(
            OUTPUT_FOLDER,
            "department_summary.xlsx"
        ),
        index=False
    )

    print("✓ department_summary.xlsx exported")


def export_summary_report(df: pd.DataFrame) -> None:
    """
    Export overall summary statistics.
    """

    summary = pd.DataFrame({

        "Metric": [

            "Total Students",
            "Average CGPA",
            "Average Percentage",
            "Average Attendance",
            "Placement Eligible",
            "Scholarship Students",
            "Hostellers",
            "Average Study Hours",
            "Average Internet Usage"

        ],

        "Value": [

            len(df),

            round(df["CGPA"].mean(), 2),

            round(df["Percentage"].mean(), 2),

            round(
                df["Attendance_Percentage"].mean(),
                2
            ),

            (df["Placement_Eligible"] == "Yes").sum(),

            (df["Scholarship"] == "Yes").sum(),

            (df["Hosteller"] == "Yes").sum(),

            round(
                df["Study_Hours_Per_Day"].mean(),
                2
            ),

            round(
                df["Internet_Usage_Hours"].mean(),
                2
            )

        ]

    })

    summary.to_excel(

        os.path.join(
            OUTPUT_FOLDER,
            "summary_report.xlsx"
        ),

        index=False

    )

    print("✓ summary_report.xlsx exported")


def export_all_reports(df: pd.DataFrame) -> None:
    """
    Export all reports.
    """

    print("\n" + "=" * 60)
    print("EXPORTING REPORTS")
    print("=" * 60)

    export_top_students(df)
    export_placement_students(df)
    export_failed_students(df)
    export_department_summary(df)
    export_summary_report(df)

    print("\nAll reports exported successfully.")