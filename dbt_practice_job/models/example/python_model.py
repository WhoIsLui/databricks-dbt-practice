

def model(dbt, session):
    print(__name__)
    df = dbt.ref('my_first_dbt_model')
    df = df.withColumn('new_column', 1)
    return df