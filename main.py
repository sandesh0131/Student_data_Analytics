"""
main.py

Student Data Analytics System
"""

from src.load_data import load_dataset
from src.initial_exploration import (
    dataset_shape,
    display_columns,
    check_data_types,
    dataset_information,
    memory_usage,
    summary_statistics,
    categorical_summary,
    initial_observations
)

from src.cleaning import (
    handle_missing_values,
    remove_duplicate_records,
    standardize_column_names,
    clean_string_columns,
    standardize_text_values,
    convert_data_types,
    export_cleaned_dataset
)

from src.numpy_analysis import (
    dataframe_to_numpy,
    basic_statistics,
    array_slicing,
    high_performers,
    attendance_filter,
    sort_percentages,
    random_sample,
    assignment_bonus,
    academic_average,
    percentile_analysis,
    department_random_sample,
    cgpa_distribution,
    marks_statistics
)

from src.pandas_analysis import (
    filter_high_cgpa_students,
    filter_low_attendance,
    sort_by_percentage,
    department_summary,
    attendance_summary,
    pivot_department_year,
    scholarship_crosstab,
    placement_query,
    grade_value_counts,
    cgpa_rank,
    attendance_transform,
    merge_example
)

from src.performance_analysis import (
    top_10_students,
    department_toppers,
    average_cgpa,
    attendance_analysis,
    scholarship_analysis,
    placement_analysis,
    hosteller_analysis,
    backlog_analysis,
    department_performance,
    city_performance,
    course_performance,
    study_hours_analysis,
    internet_usage_analysis,
    library_analysis,
    sports_analysis,
    family_income_analysis
)

from src.business_questions import run_business_analysis
from src.visualization import generate_all_visualizations
from src.export_reports import export_all_reports


DATASET_PATH = "data/students.xlsx"
CLEANED_DATASET_PATH = "data/cleaned_students.xlsx"

student_df = None


# =====================================================
# Load Dataset
# =====================================================

def load_data():

    global student_df

    student_df = load_dataset(DATASET_PATH)

    print("\nDataset Loaded Successfully.")
    print(student_df.shape)


# =====================================================
# Initial Exploration
# =====================================================

def explore_data():

    if student_df is None:
        print("\nPlease load the dataset first.")
        return

    dataset_shape(student_df)
    display_columns(student_df)
    check_data_types(student_df)
    dataset_information(student_df)
    memory_usage(student_df)
    summary_statistics(student_df)
    categorical_summary(student_df)
    initial_observations(student_df)


# =====================================================
# Data Cleaning
# =====================================================

def clean_data():

    global student_df

    if student_df is None:
        print("\nPlease load the dataset first.")
        return

    student_df = standardize_column_names(student_df)
    student_df = handle_missing_values(student_df)
    student_df = remove_duplicate_records(student_df)
    student_df = clean_string_columns(student_df)
    student_df = standardize_text_values(student_df)
    student_df = convert_data_types(student_df)

    export_cleaned_dataset(
        student_df,
        CLEANED_DATASET_PATH
    )

    print("\nCleaning Completed Successfully.")


# =====================================================
# NumPy Analysis
# =====================================================

def numpy_analysis():

    global student_df

    if student_df is None:
        print("\nPlease load the dataset first.")
        return

    dataframe_to_numpy(student_df)
    basic_statistics(student_df)
    array_slicing(student_df)
    high_performers(student_df)
    attendance_filter(student_df)
    sort_percentages(student_df)
    random_sample(student_df)
    assignment_bonus(student_df)
    student_df = academic_average(student_df)
    percentile_analysis(student_df)
    department_random_sample(student_df)
    cgpa_distribution(student_df)
    marks_statistics(student_df)


# =====================================================
# Pandas Analysis
# =====================================================

def pandas_analysis():

    if student_df is None:
        print("\nPlease load the dataset first.")
        return

    filter_high_cgpa_students(student_df)
    filter_low_attendance(student_df)
    sort_by_percentage(student_df)
    department_summary(student_df)
    attendance_summary(student_df)
    pivot_department_year(student_df)
    scholarship_crosstab(student_df)
    placement_query(student_df)
    grade_value_counts(student_df)
    cgpa_rank(student_df)
    attendance_transform(student_df)
    merge_example(student_df)


# =====================================================
# Performance Analysis
# =====================================================

def performance():

    if student_df is None:
        print("\nPlease load the dataset first.")
        return

    top_10_students(student_df)
    department_toppers(student_df)
    average_cgpa(student_df)
    attendance_analysis(student_df)
    scholarship_analysis(student_df)
    placement_analysis(student_df)
    hosteller_analysis(student_df)
    backlog_analysis(student_df)
    department_performance(student_df)
    city_performance(student_df)
    course_performance(student_df)
    study_hours_analysis(student_df)
    internet_usage_analysis(student_df)
    library_analysis(student_df)
    sports_analysis(student_df)
    family_income_analysis(student_df)


# =====================================================
# Business Questions
# =====================================================

def business_questions():

    if student_df is None:
        print("\nPlease load the dataset first.")
        return

    run_business_analysis(student_df)


# =====================================================
# Visualization
# =====================================================

def visualization():

    if student_df is None:
        print("\nPlease load the dataset first.")
        return

    generate_all_visualizations(student_df)


# =====================================================
# Export Reports
# =====================================================

def reports():

    if student_df is None:
        print("\nPlease load the dataset first.")
        return

    export_all_reports(student_df)


# =====================================================
# Run Complete Project
# =====================================================

def run_complete_project():

    load_data()
    explore_data()
    clean_data()
    numpy_analysis()
    pandas_analysis()
    performance()
    business_questions()
    visualization()
    reports()

    print("\nProject Executed Successfully.")


# =====================================================
# Menu
# =====================================================

def show_menu():

    print("\n" + "=" * 60)
    print(" STUDENT DATA ANALYTICS SYSTEM ")
    print("=" * 60)

    print("1. Load Dataset")
    print("2. Initial Exploration")
    print("3. Data Cleaning")
    print("4. NumPy Analysis")
    print("5. Pandas Analysis")
    print("6. Student Performance Analysis")
    print("7. Business Questions")
    print("8. Data Visualization")
    print("9. Export Reports")
    print("10. Run Complete Project")
    print("0. Exit")


# =====================================================
# Main
# =====================================================

def main():

    while True:

        show_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            load_data()

        elif choice == "2":
            explore_data()

        elif choice == "3":
            clean_data()

        elif choice == "4":
            numpy_analysis()

        elif choice == "5":
            pandas_analysis()

        elif choice == "6":
            performance()

        elif choice == "7":
            business_questions()

        elif choice == "8":
            visualization()

        elif choice == "9":
            reports()

        elif choice == "10":
            run_complete_project()

        elif choice == "0":
            print("\nThank you for using Student Data Analytics System.")
            break

        else:
            print("\nInvalid Choice. Please try again.")


if __name__ == "__main__":
    main()