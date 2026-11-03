import employee_info

# Test get_employees_by_age_range()
def test_get_employees_by_age_range():
    result = employee_info.get_employees_by_age_range(25, 35)

    assert len(result) == 2
    assert result[0]["name"] == "John"
    assert result[1]["name"] == "Mike"


# Test calculate_average_salary()
def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()

    assert result == 60166.666666666664


# Test get_employees_by_dept()
def test_get_employees_by_dept():
    result = employee_info.get_employees_by_dept("Engineering")

    assert len(result) == 2
    assert result[0]["name"] == "Chloe"
    assert result[1]["name"] == "Mike"
    