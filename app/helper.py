import datetime
import json
import typing

import snowflake.connector

import db

def test(**kwargs):
    print(f"Get a '{db.execute('SELECT 2;')[0][0]}' "
          f"from Snowflake at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.")


def remove_schemata(target='prod', credentials: dict = None, **kwargs) -> None:
    select_cmd = f"""
    SELECT schema_name FROM {target}_DB.INFORMATION_SCHEMA.SCHEMATA
    WHERE SCHEMA_NAME NOT IN ('PUBLIC', 'INFORMATION_SCHEMA');
    """
    print(f'Query schemata in {target}_db...')
    credentials = db.get_credentials(credentials)
    with snowflake.connector.connect(**credentials) as conn:
        with conn.cursor() as cursor:
            schemata = [row[0] for row in cursor.execute(select_cmd).fetchall()]
            drop_cmds = [
                f'DROP SCHEMA IF EXISTS {target}_DB.{schema} CASCADE;'
                for schema in schemata
            ]
            for cmd in drop_cmds:
                print(cmd)
                cursor.execute(cmd)


def get_table_stats(database: str, schema: str, credentials: dict = None, **kwargs) -> typing.List[dict]:
    credentials = db.get_credentials(credentials)
    with snowflake.connector.connect(**credentials) as conn:
        with conn.cursor(snowflake.connector.DictCursor) as cursor:
            result = []
            cursor.execute(
                f"""SELECT TABLE_NAME, COLUMN_NAME FROM {database}.INFORMATION_SCHEMA.COLUMNS WHERE 
                LOWER(TABLE_SCHEMA)='{schema.lower()}' ORDER BY TABLE_NAME, COLUMN_NAME"""
            )
            print(f'Query columns from {database}.{schema}...')
            rows = cursor.fetchall()
            for row in rows:
                print('{TABLE_NAME}.{COLUMN_NAME}'.format(**row))
                cmd = """
                SELECT '{TABLE_NAME}' AS table_name,
                       '{COLUMN_NAME}' AS column_name,
                       unique_values,
                       (unique_values/total)::FLOAT8 AS rel_unique_values,
                       non_null_values,
                       (non_null_values/total)::FLOAT8 AS rel_non_null_values,
                       total
                FROM (
                    SELECT COUNT(*) AS unique_values FROM
                    (
                        SELECT 1
                        FROM {database}.{schema_name}.{TABLE_NAME}
                        GROUP BY {COLUMN_NAME}
                        HAVING COUNT(*) = 1
                    )
                ) t1,
                (
                    SELECT COUNT(*) AS total, COUNT({COLUMN_NAME}) AS non_null_values
                    FROM {database}.{schema_name}.{TABLE_NAME}
                ) t2
                """.format(**row, database=database, schema_name=schema)
                cursor.execute(cmd)
                result.append(cursor.fetchone())

    print(json.dumps(result, indent=4))
    return result


def graph_to_svg() -> None:
    import networkx
    dag = networkx.read_gpickle('target/graph.gpickle')
    g = networkx.MultiDiGraph()
    g.add_nodes_from(
        node for node in dag.nodes if not node.startswith('test.'))
    g.add_edges_from(
        edge for edge in dag.edges if not edge[1].startswith('test.'))
    networkx.drawing.nx_pydot.to_pydot(g).write_svg('target/graph.svg')
