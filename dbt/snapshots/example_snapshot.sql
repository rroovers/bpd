{% snapshot example_snapshot %}

{{
    config(
      target_database=this.database,
      target_schema='snapshots',
      unique_key='id',
      strategy='check',
      check_cols='all',
    )
}}

select * from {{ ref('example_star')}}

{% endsnapshot %}