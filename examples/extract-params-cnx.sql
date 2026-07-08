-- Export the connectivity parameters "params-cnx.csv"
SELECT 
b.row_wid as "param_wid",
b.etl_defn_wid as "plan_wid", --execution plan id
b.name as "name",
b.value as "value",
b.copy_num as "copy_num",
b.src_delay as "src_delay",
b.type_cd as "type_cd",
b.prune_days as "prune_days", --value IS IN minutes. E.g. 2,880 = 2 days
b.app_wid as "source_system_container",
b.last_upd as "last_upd",
b.inactive_flg as "inactive_flg",
b.comments as "comments",
b.version_id as "version_id"
FROM 
ORACLEDAC.w_etl_defn_prm b;