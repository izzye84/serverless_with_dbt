{{
  config(
    materialized = 'incremental',
    unique_key = 'order_date',
    incremental_strategy="delete+insert",
    )
}}

with source as (

    {#-
    Normally we would select from the table here, but we are using seeds to load
    our data in this project
    #}
    select * from {{ ref('raw_orders') }}

),

renamed as (

    select
        id as order_id,
        user_id as customer_id,
        order_date,
        status

    from source

    -- Use the Dagster partition variables to filter rows on an incremental run
    {% if is_incremental() %}
    where order_date >= '{{ var('min_date') }}' and order_date <= '{{ var('max_date') }}'
    {% endif %}

)

select * from renamed
