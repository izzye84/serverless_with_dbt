from dagster import (
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_package_module,
)
from dagster_dbt import DbtCliResource

from . import assets
from .project import my_dbt_project

daily_refresh_schedule = ScheduleDefinition(
    job=define_asset_job(name="all_assets_job"), cron_schedule="0 0 * * *"
)

defs = Definitions(
    assets=load_assets_from_package_module(assets),
    resources={
        "dbt": DbtCliResource(project_dir=my_dbt_project),
    },
    schedules=[daily_refresh_schedule]
)
