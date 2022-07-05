import os

import snowflake.connector
import yaml


def execute(cmd: str) -> list:
    with get_conn() as conn:
        with conn.cursor() as cursor:
            for part in cmd.split(';'):
                if part.strip():
                    try:
                        cursor.execute(part)
                    except snowflake.connector.errors.ProgrammingError as e:
                        print(part)
                        raise e
            result = cursor.fetchall()
    return result


def get_credentials(args=None, target='prod'):
    if args is None:
        with open(os.path.expanduser('~/.dbt/profiles.yml')) as f:
            profile = yaml.load(f, Loader=yaml.FullLoader)
        args = {
            key: profile['bpd_woningfonds']['outputs'][target][key]
            for key in ('user', 'password', 'account', 'warehouse')
        }
    if 'SNOWFLAKE_PASSWORD' in args['password']:
        args['password'] = os.getenv('SNOWFLAKE_PASSWORD')
    if 'SNOWFLAKE_USER' in args['user']:
        args['user'] = 'dbt'
    return args


def get_conn() -> snowflake.connector.SnowflakeConnection:
    return snowflake.connector.connect(**get_credentials())
