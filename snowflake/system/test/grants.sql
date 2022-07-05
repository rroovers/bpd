use database test_db;
grant usage on database test_db to role watcher;
grant usage on future schemas in database test_db to role watcher;
grant usage on all schemas in database test_db to role watcher;
grant select on all tables in database test_db to role watcher;
grant select on future tables in database test_db to role watcher;
grant select on all views in database test_db to role watcher;
grant select on future views in database test_db to role watcher;

use database test_sources;
grant usage on database test_sources to role watcher;
grant usage on all schemas in database test_sources to role watcher;
grant usage on future schemas in database test_sources to role watcher;
grant select on all tables in database test_sources to role watcher;
grant select on future tables in database test_sources to role watcher;
grant select on all views in database test_sources to role watcher;
grant select on future views in database test_sources to role watcher;