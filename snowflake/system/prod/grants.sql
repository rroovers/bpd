use database prod_db;
grant usage on database prod_db to role watcher;
grant usage on future schemas in database prod_db to role watcher;
grant usage on all schemas in database prod_db to role watcher;
grant select on all tables in database prod_db to role watcher;
grant select on future tables in database prod_db to role watcher;
grant select on all views in database prod_db to role watcher;
grant select on future views in database prod_db to role watcher;

use database prod_sources;
grant usage on database prod_sources to role watcher;
grant usage on all schemas in database prod_sources to role watcher;
grant usage on future schemas in database prod_sources to role watcher;
grant select on all tables in database prod_sources to role watcher;
grant select on future tables in database prod_sources to role watcher;
grant select on all views in database prod_sources to role watcher;
grant select on future views in database prod_sources to role watcher;