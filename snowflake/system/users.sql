-- technical accounts
create user dbt
password = ''
login_name = 'dbt'
display_name = 'dbt Technical Account'
email = ''
default_role = "SYSADMIN"
must_change_password = FALSE;
grant role "SYSADMIN" to user dbt;

create user adf
password = ''
login_name = 'adf'
display_name = 'adf Technical Account'
email = ''
default_role = "SYSADMIN"
must_change_password = FALSE;
grant role "SYSADMIN" to user adf;


-- users
create user jgerretsen
password = 'Snowflake'
login_name = 'jgerretsen'
display_name = 'Jurri Gerretsen'
email = 'jurri.gerretsen@deptagency.com'
default_role = "SYSADMIN"
must_change_password = TRUE;
grant role "SYSADMIN" to user jgerretsen;

create user zhubai
password = 'Snowflake'
login_name = 'zhubai'
display_name = 'Zsolt Hubai'
email = 'zsolt.hubai@deptagency.com'
default_role = "SYSADMIN"
must_change_password = TRUE;
grant role "SYSADMIN" to user zhubai;

create user rroovers
password = 'Snowflake'
login_name = 'rroovers'
display_name = 'Rene Roovers'
email = 'rene@rooversconsultancy.nl'
default_role = "SYSADMIN"
must_change_password = TRUE;
grant role "SYSADMIN" to user rroovers;