{% snapshot example_source_snapshot %}

{{
    config(
      target_database=target.database,
      target_schema='snapshots',
      unique_key='id',
      strategy='check',
      check_cols='all',
    )
}}

select * from {{ source('salesforce', 'gemeente')}}

{% endsnapshot %}