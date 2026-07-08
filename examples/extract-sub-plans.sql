-- Extract task group execution plans
SELECT 
distinct	
g.ROW_WID AS "plan_wid"
, g.NAME AS "plan_name"
, g.INACTIVE_FLG AS "plan_inactive_flag"
, s.ROW_WID AS "plan_step_wid"
, m.GRP_EXEC_ORDER AS "plan_step_order"
, d.TYPE_CD AS "plan_step_type"
, g.APP_WID as "source_system_container"
, s.ROW_WID AS "step_wid"
, s.CMD_NAME AS "step_cmd"
, s.NAME AS "step_name"
, '' AS "group_name"
, e.name AS "exec_type"
FROM 
ORACLEDAC.W_ETL_STEP g
INNER JOIN ORACLEDAC.W_ETL_GROUP_STEP m
ON (g.ROW_WID = m.GROUP_WID)
INNER JOIN ORACLEDAC.W_ETL_STEP s
ON (m.step_wid = s.ROW_WID)
LEFT OUTER JOIN ORACLEDAC.W_ETL_DEFN_STEP d
ON (s.row_wid = d.STEP_WID)
LEFT OUTER JOIN ORACLEDAC.w_etl_exec_type e
ON (s.EXEC_WID = e.row_wid)
ORDER BY
g.ROW_WID,
m.GRP_EXEC_ORDER,
s.NAME