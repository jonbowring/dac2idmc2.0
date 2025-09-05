SELECT 
a.ROW_WID AS "plan_wid"
, a.NAME AS "plan_name"
, a.INACTIVE_FLG AS "plan_inactive_flag"
, b.ROW_WID AS "plan_step_wid"
, b.PRIORITY AS "plan_step_order"
, b.TYPE_CD AS "plan_step_type"
, b.APP_WID as "source_system_container"
, c.ROW_WID AS "step_wid"
, c.CMD_NAME AS "step_cmd"
, c.NAME AS "step_name"
, b.group_name AS "group_name"
, d.name AS "exec_type"
FROM 
ORACLEDAC.W_ETL_DEFN a
INNER JOIN ORACLEDAC.W_ETL_DEFN_STEP b
ON (a.ROW_WID = b.ETL_DEFN_WID)
INNER JOIN ORACLEDAC.W_ETL_STEP c
ON (b.STEP_WID = c.ROW_WID)
LEFT OUTER JOIN ORACLEDAC.w_etl_exec_type d
ON (c.EXEC_WID = d.row_wid)
ORDER BY 
a.NAME 
, b.PRIORITY 
, d.name
, c.NAME 
