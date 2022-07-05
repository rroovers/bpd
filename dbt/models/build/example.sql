{{ config(materialized=mat('table')) }}

SELECT 
    id AS gemeente_id,
    name AS gemeente_naam
     
FROM {{ source('salesforce', 'gemeente')}}