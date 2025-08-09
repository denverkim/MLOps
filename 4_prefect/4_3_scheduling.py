from datetime import timedelta
from prefect.deployments import Deployment
from prefect.server.schemas.schedules import IntervalSchedule

Deployment.build_from_flow(
    flow=etl_flow,
    name="scheduled-etl",
    schedule=IntervalSchedule(interval=timedelta(minutes=10)),
).apply()
