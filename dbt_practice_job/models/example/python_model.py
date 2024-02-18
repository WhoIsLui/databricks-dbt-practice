import dbt

def model():
    print(__name__)
    return dbt.utils.execute_query(
        "SELECT * FROM example_table"
    )