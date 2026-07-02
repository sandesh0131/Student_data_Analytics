import pandas as pd


def q1_highest_average_percentage_department(df):
    result = (
        df.groupby("Department")["Percentage"]
        .mean()
        .sort_values(ascending=False)
        .round(2)
    )

    print("\nQ1. Department with Highest Average Percentage")
    print(result.head(1))


def q2_highest_average_cgpa_department(df):
    result = (
        df.groupby("Department")["CGPA"]
        .mean()
        .sort_values(ascending=False)
        .round(2)
    )

    print("\nQ2. Department with Highest Average CGPA")
    print(result.head(1))


def q3_highest_placement_rate(df):
    result = (
        df.groupby("Department")["Placement_Eligible"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .sort_values(ascending=False)
        .round(2)
    )

    print("\nQ3. Department with Highest Placement Rate")
    print(result)


def q4_city_highest_cgpa(df):
    result = (
        df.groupby("City")["CGPA"]
        .mean()
        .sort_values(ascending=False)
        .round(2)
    )

    print("\nQ4. City with Highest Average CGPA")
    print(result.head(10))


def q5_students_need_attendance_improvement(df):
    result = df[df["Attendance_Percentage"] < 75]

    print("\nQ5. Students Needing Attendance Improvement")
    print(result[["Student_ID", "Attendance_Percentage"]].head(10))


def q6_scholarship_students(df):
    result = df[df["Scholarship"] == "Yes"]

    print("\nQ6. Scholarship Students")
    print(result[["Student_ID", "CGPA", "Percentage"]].head(10))


def q7_department_backlogs(df):
    result = (
        df.groupby("Department")["Backlogs"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nQ7. Department-wise Backlogs")
    print(result)


def q8_hosteller_vs_day_scholar(df):
    result = (
        df.groupby("Hosteller")["CGPA"]
        .mean()
        .round(2)
    )

    print("\nQ8. Hosteller vs Day Scholar")
    print(result)


def q9_average_study_hours(df):
    result = (
        df.groupby("Department")["Study_Hours_Per_Day"]
        .mean()
        .round(2)
    )

    print("\nQ9. Average Study Hours")
    print(result)


def q10_library_visits(df):
    result = (
        df.groupby("Department")["Library_Visits"]
        .mean()
        .round(2)
    )

    print("\nQ10. Average Library Visits")
    print(result)


def q11_average_internet_usage(df):
    result = (
        df.groupby("Department")["Internet_Usage_Hours"]
        .mean()
        .round(2)
    )

    print("\nQ11. Internet Usage")
    print(result)


def q12_gender_distribution(df):
    print("\nQ12. Gender Distribution")
    print(df["Gender"].value_counts())


def q13_grade_distribution(df):
    print("\nQ13. Grade Distribution")
    print(df["Grade"].value_counts())


def q14_result_distribution(df):
    print("\nQ14. Result Distribution")
    print(df["Result"].value_counts())


def q15_average_marks(df):
    columns = [
        "Assignment_Marks",
        "Internal_Marks",
        "Midterm_Marks",
        "Final_Exam_Marks"
    ]

    print("\nQ15. Average Marks")
    print(df[columns].mean().round(2))


def q16_top_5_students(df):
    result = (
        df.sort_values("CGPA", ascending=False)
        .head(5)
    )

    print("\nQ16. Top 5 Students")
    print(result[["Student_ID", "CGPA"]])


def q17_bottom_5_students(df):
    result = (
        df.sort_values("CGPA")
        .head(5)
    )

    print("\nQ17. Bottom 5 Students")
    print(result[["Student_ID", "CGPA"]])


def q18_department_strength(df):
    print("\nQ18. Department Strength")
    print(df["Department"].value_counts())


def q19_state_strength(df):
    print("\nQ19. State-wise Students")
    print(df["State"].value_counts())


def q20_transport_mode(df):
    print("\nQ20. Transport Mode")
    print(df["Transport_Mode"].value_counts())


def q21_extra_curricular(df):
    print("\nQ21. Extra Curricular Activities")
    print(df["Extra_Curricular"].value_counts())


def q22_average_family_income(df):
    result = (
        df.groupby("Department")["Family_Income"]
        .mean()
        .round(2)
    )

    print("\nQ22. Average Family Income")
    print(result)


def q23_internship_students(df):
    result = df[df["Internship"] == "Yes"]

    print("\nQ23. Internship Students")
    print(result[["Student_ID", "Department"]].head(10))


def q24_students_with_backlogs(df):
    result = df[df["Backlogs"] > 0]

    print("\nQ24. Students with Backlogs")
    print(result[["Student_ID", "Backlogs"]].head(10))


def q25_department_wise_result(df):
    result = pd.crosstab(
        df["Department"],
        df["Result"]
    )

    print("\nQ25. Department-wise Result")
    print(result)


def run_business_analysis(df):
    """
    Run all business questions sequentially.
    """

    analyses = [
        q1_highest_average_percentage_department,
        q2_highest_average_cgpa_department,
        q3_highest_placement_rate,
        q4_city_highest_cgpa,
        q5_students_need_attendance_improvement,
        q6_scholarship_students,
        q7_department_backlogs,
        q8_hosteller_vs_day_scholar,
        q9_average_study_hours,
        q10_library_visits,
        q11_average_internet_usage,
        q12_gender_distribution,
        q13_grade_distribution,
        q14_result_distribution,
        q15_average_marks,
        q16_top_5_students,
        q17_bottom_5_students,
        q18_department_strength,
        q19_state_strength,
        q20_transport_mode,
        q21_extra_curricular,
        q22_average_family_income,
        q23_internship_students,
        q24_students_with_backlogs,
        q25_department_wise_result,
    ]

    for analysis in analyses:
        analysis(df)