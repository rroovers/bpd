import argparse
import helper

credentials = {
    'user': 'dbt',
    'account': 'ai43988.west-europe.azure',
    'warehouse': 'DEV_WH'
}


def parse(args=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Run SQL helper.')
    parser.add_argument('function', type=str, help='function')
    parser.add_argument('--target', help='dbt target')
    parser.add_argument('--database', help='database name')
    parser.add_argument('--schema', help='schema name')
    return parser.parse_args(args)


def run():
    args = parse()
    f = getattr(helper, args.function.replace('-', '_'))
    f(**vars(args))


if __name__ == "__main__":
    run()
