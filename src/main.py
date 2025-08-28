#!/usr/bin/env python3
"""
Main application file for pandas-spss project.
Demonstrates basic pandas functionality.
"""

import pandas as pd
import numpy as np
from typing import Dict


def create_sample_data() -> pd.DataFrame:
    """Create sample data for demonstration."""
    np.random.seed(42)

    data = {
        "id": range(1, 101),
        "name": [f"User_{i}" for i in range(1, 101)],
        "age": np.random.randint(18, 80, 100),
        "salary": np.random.normal(50000, 15000, 100),
        "department": np.random.choice(
            ["Engineering", "Sales", "Marketing", "HR"], 100
        ),
        "experience_years": np.random.randint(0, 20, 100),
    }

    return pd.DataFrame(data)


def analyze_data(df: pd.DataFrame) -> Dict[str, any]:
    """Analyze the sample data and return summary statistics."""
    analysis = {
        "total_employees": len(df),
        "avg_age": df["age"].mean(),
        "avg_salary": df["salary"].mean(),
        "department_counts": df["department"].value_counts().to_dict(),
        "salary_by_department": df.groupby("department")["salary"]
        .agg(["mean", "std"])
        .to_dict("index"),
        "correlation_age_salary": df["age"].corr(df["salary"]),
    }

    return analysis


def main():
    """Main function to demonstrate pandas functionality."""
    print("🐼 pandas-spss Project")
    print("=" * 50)

    # Create sample data
    print("Creating sample employee data...")
    df = create_sample_data()

    # Display basic info
    print(f"\nDataset shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")

    # Show first few rows
    print("\nFirst 5 rows:")
    print(df.head())

    # Analyze data
    print("\nAnalyzing data...")
    analysis = analyze_data(df)

    # Display analysis results
    print("\n📊 Analysis Results:")
    print(f"Total employees: {analysis['total_employees']}")
    print(f"Average age: {analysis['avg_age']:.1f} years")
    print(f"Average salary: ${analysis['avg_salary']:,.2f}")
    print(f"Age-Salary correlation: {analysis['correlation_age_salary']:.3f}")

    print("\n👥 Department Distribution:")
    for dept, count in analysis["department_counts"].items():
        print(f"  {dept}: {count} employees")

    print("\n💰 Average Salary by Department:")
    for dept, stats in analysis["salary_by_department"].items():
        print(f"  {dept}: ${stats['mean']:,.2f} (±${stats['std']:,.2f})")

    # Save to CSV
    output_file = "employee_data.csv"
    df.to_csv(output_file, index=False)
    print(f"\n💾 Data saved to {output_file}")

    print("\n✅ pandas demonstration completed!")


if __name__ == "__main__":
    main()
