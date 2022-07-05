create role watcher comment = 'Read-only on all tables';
grant usage on warehouse dev_wh to role watcher;
grant role watcher to role sysadmin;