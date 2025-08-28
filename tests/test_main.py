"""
Tests for the main module.
"""

import os
import sys

import pandas as pd
import pytest  # noqa: F401

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from main import create_sample_data, analyze_data  # noqa: E402


class TestMain:
    """Test class for main module functions."""

    def test_create_sample_data(self):
        """Test that sample data is created correctly."""
        df = create_sample_data()

        # Check that it's a DataFrame
        assert isinstance(df, pd.DataFrame)

        # Check expected columns
        expected_columns = [
            "id",
            "name",
            "age",
            "salary",
            "department",
            "experience_years",
        ]
        assert list(df.columns) == expected_columns

        # Check data types
        assert df["id"].dtype == "int64"
        assert df["name"].dtype == "object"
        assert df["age"].dtype == "int64"
        assert df["salary"].dtype == "float64"
        assert df["department"].dtype == "object"
        assert df["experience_years"].dtype == "int64"

        # Check data ranges
        assert len(df) == 100
        assert df["age"].min() >= 18
        assert df["age"].max() < 80
        assert df["experience_years"].min() >= 0
        assert df["experience_years"].max() < 20

        # Check department values
        expected_departments = ["Engineering", "Sales", "Marketing", "HR"]
        assert all(
            dept in expected_departments for dept in df["department"].unique()
        )

    def test_analyze_data(self):
        """Test that data analysis works correctly."""
        df = create_sample_data()
        analysis = analyze_data(df)

        # Check that analysis returns a dict
        assert isinstance(analysis, dict)

        # Check required keys
        required_keys = [
            "total_employees",
            "avg_age",
            "avg_salary",
            "department_counts",
            "salary_by_department",
            "correlation_age_salary",
        ]
        for key in required_keys:
            assert key in analysis

        # Check data types and values
        assert isinstance(analysis["total_employees"], int)
        assert analysis["total_employees"] == 100

        assert isinstance(analysis["avg_age"], float)
        assert 18 <= analysis["avg_age"] <= 80

        assert isinstance(analysis["avg_salary"], float)
        assert analysis["avg_salary"] > 0

        assert isinstance(analysis["department_counts"], dict)
        assert len(analysis["department_counts"]) == 4

        assert isinstance(analysis["salary_by_department"], dict)
        assert len(analysis["salary_by_department"]) == 4

        assert isinstance(analysis["correlation_age_salary"], float)
        assert -1 <= analysis["correlation_age_salary"] <= 1

    def test_data_consistency(self):
        """Test that the same seed produces consistent results."""
        # This test might fail if numpy seed isn't set properly
        # but it's good to have for regression testing
        df1 = create_sample_data()
        df2 = create_sample_data()

        # Check that data is consistent (same seed)
        pd.testing.assert_frame_equal(df1, df2)
