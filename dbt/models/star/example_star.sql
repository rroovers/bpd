{{ config(materialized=mat('view')) }}

SELECT * FROM {{ ref('example')}}