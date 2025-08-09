from prefect import flow, task


@task
def extract():
    data = [1, 2, 3, 4, 5]
    return data


@task
def transform(data):
    return [x * 2 for x in data]


@task
def load(data):
    print(f"Loaded data: {data}")


@flow
def etl_flow():
    raw_data = extract()
    transformed = transform(raw_data)
    load(transformed)


if __name__ == "__main__":
    etl_flow()
