"""
visualization.py

Professional Data Visualizations for Student Data Analytics System
Author: Sandesh Dhadam
"""

import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# -------------------------------------------------------
# Global Configuration
# -------------------------------------------------------

plt.style.use("ggplot")
sns.set_theme(style="whitegrid")

OUTPUT_FOLDER = "charts"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def save_chart(file_name: str) -> None:
    """
    Save the current chart into the charts folder.
    """

    plt.tight_layout()

    plt.savefig(
        os.path.join(OUTPUT_FOLDER, file_name),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


# =======================================================
# 1. Correlation Heatmap
# =======================================================

def correlation_heatmap(df: pd.DataFrame) -> None:
    """
    Business Question:
    Which numerical variables are highly correlated?
    """

    plt.figure(figsize=(14, 10))

    numerical_df = df.select_dtypes(include="number")

    sns.heatmap(
        numerical_df.corr(),
        cmap="coolwarm",
        annot=True,
        fmt=".2f",
        linewidths=0.5
    )

    plt.title("Correlation Heatmap", fontsize=16)
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)

    save_chart("01_correlation_heatmap.png")


# =======================================================
# 2. Department-wise Average CGPA
# =======================================================

def department_average_cgpa(df: pd.DataFrame) -> None:
    """
    Business Question:
    Which department performs best academically?
    """

    department_cgpa = (
        df.groupby("Department")["CGPA"]
        .mean()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 6))

    department_cgpa.plot(
        kind="bar",
        edgecolor="black"
    )

    plt.title("Department-wise Average CGPA")
    plt.xlabel("Department")
    plt.ylabel("Average CGPA")
    plt.xticks(rotation=30)

    save_chart("02_department_average_cgpa.png")


# =======================================================
# 3. Attendance Distribution
# =======================================================

def attendance_histogram(df: pd.DataFrame) -> None:
    """
    Business Question:
    How is attendance distributed among students?
    """

    plt.figure(figsize=(9, 6))

    sns.histplot(
        data=df,
        x="Attendance_Percentage",
        bins=20,
        kde=True
    )

    plt.title("Attendance Percentage Distribution")
    plt.xlabel("Attendance Percentage")
    plt.ylabel("Number of Students")

    save_chart("03_attendance_distribution.png")


# =======================================================
# 4. CGPA Distribution
# =======================================================

def cgpa_histogram(df: pd.DataFrame) -> None:
    """
    Business Question:
    What is the distribution of CGPA?
    """

    plt.figure(figsize=(9, 6))

    sns.histplot(
        data=df,
        x="CGPA",
        bins=20,
        kde=True
    )

    plt.title("CGPA Distribution")
    plt.xlabel("CGPA")
    plt.ylabel("Students")

    save_chart("04_cgpa_distribution.png")


# =======================================================
# 5. Study Hours vs CGPA
# =======================================================

def study_hours_vs_cgpa(df: pd.DataFrame) -> None:
    """
    Business Question:
    Does studying more improve CGPA?
    """

    plt.figure(figsize=(9, 6))

    sns.scatterplot(
        data=df,
        x="Study_Hours_Per_Day",
        y="CGPA",
        alpha=0.7
    )

    plt.title("Study Hours vs CGPA")
    plt.xlabel("Study Hours Per Day")
    plt.ylabel("CGPA")

    save_chart("05_study_hours_vs_cgpa.png")

# =======================================================
# 6. Internet Usage vs CGPA
# =======================================================

def internet_usage_vs_cgpa(df: pd.DataFrame) -> None:
    """
    Business Question:
    Does internet usage affect academic performance?
    """

    plt.figure(figsize=(9, 6))

    sns.scatterplot(
        data=df,
        x="Internet_Usage_Hours",
        y="CGPA",
        alpha=0.7
    )

    plt.title("Internet Usage vs CGPA")
    plt.xlabel("Internet Usage (Hours/Day)")
    plt.ylabel("CGPA")

    save_chart("06_internet_usage_vs_cgpa.png")


# =======================================================
# 7. Library Visits vs CGPA
# =======================================================

def library_visits_vs_cgpa(df: pd.DataFrame) -> None:
    """
    Business Question:
    Do students who visit the library more perform better?
    """

    plt.figure(figsize=(9, 6))

    sns.scatterplot(
        data=df,
        x="Library_Visits",
        y="CGPA",
        alpha=0.7
    )

    plt.title("Library Visits vs CGPA")
    plt.xlabel("Library Visits")
    plt.ylabel("CGPA")

    save_chart("07_library_visits_vs_cgpa.png")


# =======================================================
# 8. Department-wise Percentage Distribution
# =======================================================

def department_percentage_boxplot(df: pd.DataFrame) -> None:
    """
    Business Question:
    How does student percentage vary across departments?
    """

    plt.figure(figsize=(12, 6))

    sns.boxplot(
        data=df,
        x="Department",
        y="Percentage"
    )

    plt.title("Department-wise Percentage Distribution")
    plt.xlabel("Department")
    plt.ylabel("Percentage")

    plt.xticks(rotation=30)

    save_chart("08_department_percentage_boxplot.png")


# =======================================================
# 9. Gender Distribution
# =======================================================

def gender_distribution(df: pd.DataFrame) -> None:
    """
    Business Question:
    What is the gender distribution of students?
    """

    gender_count = df["Gender"].value_counts()

    plt.figure(figsize=(7, 7))

    plt.pie(
        gender_count,
        labels=gender_count.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Gender Distribution")

    save_chart("09_gender_distribution.png")


# =======================================================
# 10. Grade Distribution
# =======================================================

def grade_distribution(df: pd.DataFrame) -> None:
    """
    Business Question:
    How are grades distributed among students?
    """

    plt.figure(figsize=(9, 6))

    sns.countplot(
        data=df,
        x="Grade",
        order=sorted(df["Grade"].dropna().unique())
    )

    plt.title("Grade Distribution")
    plt.xlabel("Grade")
    plt.ylabel("Number of Students")

    save_chart("10_grade_distribution.png")

# =======================================================
# 11. Placement Eligibility Distribution
# =======================================================

def placement_distribution(df: pd.DataFrame) -> None:
    """
    Business Question:
    How many students are placement eligible?
    """

    plt.figure(figsize=(8, 6))

    sns.countplot(
        data=df,
        x="Placement_Eligible"
    )

    plt.title("Placement Eligibility Distribution")
    plt.xlabel("Placement Eligible")
    plt.ylabel("Number of Students")

    save_chart("11_placement_distribution.png")


# =======================================================
# 12. Hosteller vs CGPA
# =======================================================

def hosteller_vs_cgpa(df: pd.DataFrame) -> None:
    """
    Business Question:
    Do hostellers perform better than day scholars?
    """

    plt.figure(figsize=(8, 6))

    sns.violinplot(
        data=df,
        x="Hosteller",
        y="CGPA"
    )

    plt.title("Hosteller vs CGPA")
    plt.xlabel("Hosteller")
    plt.ylabel("CGPA")

    save_chart("12_hosteller_vs_cgpa.png")


# =======================================================
# 13. Department Strength
# =======================================================

def department_strength(df: pd.DataFrame) -> None:
    """
    Business Question:
    Which department has the highest number of students?
    """

    plt.figure(figsize=(11, 6))

    sns.countplot(
        data=df,
        x="Department",
        order=df["Department"].value_counts().index
    )

    plt.title("Department-wise Student Strength")
    plt.xlabel("Department")
    plt.ylabel("Number of Students")

    plt.xticks(rotation=30)

    save_chart("13_department_strength.png")


# =======================================================
# 14. Result Distribution
# =======================================================

def result_distribution(df: pd.DataFrame) -> None:
    """
    Business Question:
    What is the overall result distribution?
    """

    plt.figure(figsize=(8, 6))

    sns.countplot(
        data=df,
        x="Result",
        order=df["Result"].value_counts().index
    )

    plt.title("Result Distribution")
    plt.xlabel("Result")
    plt.ylabel("Number of Students")

    save_chart("14_result_distribution.png")


# =======================================================
# 15. Average Percentage by Year
# =======================================================

def year_percentage(df: pd.DataFrame) -> None:
    """
    Business Question:
    How does average percentage vary by academic year?
    """

    year_avg = (
        df.groupby("Year")["Percentage"]
        .mean()
        .sort_index()
    )

    plt.figure(figsize=(8, 6))

    plt.plot(
        year_avg.index,
        year_avg.values,
        marker="o",
        linewidth=2
    )

    plt.title("Average Percentage by Year")
    plt.xlabel("Academic Year")
    plt.ylabel("Average Percentage")

    plt.grid(True)

    save_chart("15_average_percentage_by_year.png")


# =======================================================
# Generate All Visualizations
# =======================================================

def generate_all_visualizations(df: pd.DataFrame) -> None:
    """
    Generate and save all visualizations.
    """

    print("\n" + "=" * 70)
    print("GENERATING VISUALIZATIONS")
    print("=" * 70)

    visualization_functions = [
        correlation_heatmap,
        department_average_cgpa,
        attendance_histogram,
        cgpa_histogram,
        study_hours_vs_cgpa,
        internet_usage_vs_cgpa,
        library_visits_vs_cgpa,
        department_percentage_boxplot,
        gender_distribution,
        grade_distribution,
        placement_distribution,
        hosteller_vs_cgpa,
        department_strength,
        result_distribution,
        year_percentage
    ]

    total_charts = len(visualization_functions)

    for index, function in enumerate(visualization_functions, start=1):
        try:
            function(df)
            print(f"[{index:02d}/{total_charts}] {function.__name__} ✓")
        except Exception as error:
            print(f"[{index:02d}/{total_charts}] {function.__name__} ✗")
            print(f"Error: {error}")

    print("\n" + "=" * 70)
    print(f"Successfully generated {total_charts} visualizations.")
    print(f"Charts saved in: {OUTPUT_FOLDER}")
    print("=" * 70)