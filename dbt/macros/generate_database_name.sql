-- Macro to generate the schema name using the following logic:

-- Scenraio 1 (if) - running without custom database:
-- This occurs when running the models cdp.*
-- The database name will equal: <default_database>

-- Scenario 2 (else):
-- When running any other models than cdp.*, the custom database name will get a prefix 'prod_' or 'test_' depending on the target.


{% macro generate_database_name(custom_database_name=none, node=none) -%}

    {%- if custom_database_name is none -%}

        {{ target.database }}

    {%- else -%}

        {{ target.name }}_{{ custom_database_name | trim }}

    {%- endif -%}

{%- endmacro %}
