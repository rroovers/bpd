-- Macro to generate the schema name using the following logic:

-- By convention, a custom schema has to be explicitly specified for each node!
-- Otherwise this macro will not work
-- Check dbt_project.yml if +schema config is added for each node.

-- Running against target 'prod':
-- -- The schema name will always be: <custom_schema>

-- Running against target 'test'
-- The schema will be different when running locally versus running it on a schedule.
-- The script will check if the default schema in profiles.yml is set to 'cdp' or not.
-- 'cdp' is just an indicator, it will not be used to name schemas
-- Thus, you should configure your local profiles.yml in ~/.dbt to have a unique name (NOT 'cdp')
-- By convention, each user should specify a unique default schema name (e.g. zhubai or jgerretsen)
-- This way we can avoid situations where the samme models are tested simultaniously.

-- -- Running locally (using ~/.dbt/profiles.yml)
-- -- The schema name will be: <default_schema>_<custom_schema>

-- -- Running on a schedule (using ./profiles.yml)
-- -- The schema name will be: <custom_schema>


{% macro generate_schema_name(custom_schema_name=none, node=none) -%}

    {%- if (target.schema == 'cdp') or (target.name != 'test')  -%}

        {{ custom_schema_name | trim }}
        
    {%- else -%}

        {{ target.schema }}_{{ custom_schema_name | trim }}

    {%- endif -%}

{%- endmacro %}
