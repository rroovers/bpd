{% macro mat(materialization) -%}

    {%- if target.name == 'check' -%}

        {{ 'view' }}

    {%- else -%}

        {{ materialization }}

    {%- endif -%}

{%- endmacro %}