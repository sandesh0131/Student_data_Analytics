"""
performance_analysis.py

Student Performance Analysis
"""

import pandas as pd


def top_10_students(df: pd.DataFrame) -> None:
    """Top 10 students based on Percentage."""

    top_students = (
        df.sort_values("Percentage", ascending=False)
        .loc[:, ["Student_ID", "First_Name", "Last_Name",
                 "Department", "CGPA", "Percentage"]]
        .head(10)
    )

    print("\n" + "=" * 70)
    print("TOP 10 STUDENTS")
    print("=" * 70)
    print(top_students)


def department_toppers(df: pd.DataFrame) -> None:
    """Find topper from every department."""

    toppers = (
        df.sort_values("Percentage", ascending=False)
        .groupby("Department")
        .head(1)
        .loc[:, [
            "Department",
            "Student_ID",
            "First_Name",
            "CGPA",
            "Percentage"
        ]]
    )

    print("\n" + "=" * 70)
    print("DEPARTMENT TOPPERS")
    print("=" * 70)
    print(toppers)


def average_cgpa(df: pd.DataFrame) -> None:
    """Overall average CGPA."""

    print("\nAverage CGPA :", round(df["CGPA"].mean(), 2))


def attendance_analysis(df: pd.DataFrame) -> None:
    """Attendance statistics."""

    print("\n" + "=" * 70)
    print("ATTENDANCE ANALYSIS")
    print("=" * 70)

    print(f"Average Attendance : {df['Attendance_Percentage'].mean():.2f}%")
    print(f"Highest Attendance : {df['Attendance_Percentage'].max()}%")
    print(f"Lowest Attendance  : {df['Attendance_Percentage'].min()}%")


def scholarship_analysis(df: pd.DataFrame) -> None:
    """Scholarship statistics."""

    scholarship = (
        df.groupby("Scholarship")
        .agg(
            Students=("Student_ID", "count"),
            Average_CGPA=("CGPA", "mean")
        )
        .round(2)
    )

    print("\n" + "=" * 70)
    print("SCHOLARSHIP ANALYSIS")
    print("=" * 70)
    print(scholarship)


def placement_analysis(df: pd.DataFrame) -> None:
    """Placement eligibility summary."""

    placement = (
        df.groupby("Placement_Eligible")
        .agg(
            Students=("Student_ID", "count"),
            Average_CGPA=("CGPA", "mean")
        )
        .round(2)
    )

    print("\n" + "=" * 70)
    print("PLACEMENT ELIGIBILITY")
    print("=" * 70)
    print(placement)


def hosteller_analysis(df: pd.DataFrame) -> None:
    """Hosteller vs Day Scholar performance."""

    hosteller = (
        df.groupby("Hosteller")
        .agg(
            Students=("Student_ID", "count"),
            Average_CGPA=("CGPA", "mean"),
            Average_Percentage=("Percentage", "mean")
        )
        .round(2)
    )

    print("\n" + "=" * 70)
    print("HOSTELLER ANALYSIS")
    print("=" * 70)
    print(hosteller)


def backlog_analysis(df: pd.DataFrame) -> None:
    """Students with backlogs."""

    backlog = (
        df.groupby("Backlogs")
        .size()
        .reset_index(name="Students")
    )

    print("\n" + "=" * 70)
    print("BACKLOG ANALYSIS")
    print("=" * 70)
    print(backlog)


def department_performance(df: pd.DataFrame) -> None:
    """Department-wise academic performance."""

    performance = (
        df.groupby("Department")
        .agg(
            Average_CGPA=("CGPA", "mean"),
            Average_Percentage=("Percentage", "mean"),
            Students=("Student_ID", "count")
        )
        .round(2)
        .sort_values("Average_CGPA", ascending=False)
    )

    print("\n" + "=" * 70)
    print("DEPARTMENT PERFORMANCE")
    print("=" * 70)
    print(performance)


def city_performance(df: pd.DataFrame) -> None:
    """City-wise performance."""

    city = (
        df.groupby("City")
        .agg(
            Average_CGPA=("CGPA", "mean"),
            Students=("Student_ID", "count")
        )
        .round(2)
        .sort_values("Average_CGPA", ascending=False)
    )

    print("\n" + "=" * 70)
    print("CITY PERFORMANCE")
    print("=" * 70)
    print(city)


def course_performance(df: pd.DataFrame) -> None:
    """Course-wise performance."""

    course = (
        df.groupby("Course")
        .agg(
            Average_CGPA=("CGPA", "mean"),
            Average_Percentage=("Percentage", "mean")
        )
        .round(2)
        .sort_values("Average_CGPA", ascending=False)
    )

    print("\n" + "=" * 70)
    print("COURSE PERFORMANCE")
    print("=" * 70)
    print(course)


def study_hours_analysis(df: pd.DataFrame) -> None:
    """Study hours vs CGPA."""

    study = (
        df.groupby("Study_Hours_Per_Day")
        .agg(
            Average_CGPA=("CGPA", "mean")
        )
        .round(2)
    )

    print("\n" + "=" * 70)
    print("STUDY HOURS VS CGPA")
    print("=" * 70)
    print(study)


def internet_usage_analysis(df: pd.DataFrame) -> None:
    """Internet usage vs CGPA."""

    internet = (
        df.groupby("Internet_Usage_Hours")
        .agg(
            Average_CGPA=("CGPA", "mean")
        )
        .round(2)
    )

    print("\n" + "=" * 70)
    print("INTERNET USAGE VS CGPA")
    print("=" * 70)
    print(internet)


def library_analysis(df: pd.DataFrame) -> None:
    """Library visits vs academic performance."""

    library = (
        df.groupby("Library_Visits")
        .agg(
            Average_CGPA=("CGPA", "mean")
        )
        .round(2)
    )

    print("\n" + "=" * 70)
    print("LIBRARY VISITS VS CGPA")
    print("=" * 70)
    print(library)


def sports_analysis(df: pd.DataFrame) -> None:
    """Sports marks analysis."""

    sports = (
        df.groupby("Department")
        .agg(
            Average_Sports_Marks=("Sports_Marks", "mean")
        )
        .round(2)
    )

    print("\n" + "=" * 70)
    print("SPORTS PERFORMANCE")
    print("=" * 70)
    print(sports)


def family_income_analysis(df: pd.DataFrame) -> None:
    """Family income vs academic performance."""

    income = (
        df.groupby("Family_Income")
        .agg(
            Average_CGPA=("CGPA", "mean")
        )
        .round(2)
    )

    print("\n" + "=" * 70)
    print("FAMILY INCOME VS PERFORMANCE")
    print("=" * 70)
    print(income)