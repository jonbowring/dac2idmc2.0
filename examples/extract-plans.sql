SELECT 
a.ROW_WID AS "plan_wid"
, a.NAME AS "plan_name"
, a.INACTIVE_FLG AS "plan_inactive_flag"
, b.ROW_WID AS "plan_step_wid"
, b.PRIORITY AS "plan_step_order"
, b.TYPE_CD AS "plan_step_type"
, c.ROW_WID AS "step_wid"
, c.CMD_NAME AS "step_cmd"
, c.NAME AS "step_name"
FROM 
ORACLEDAC.W_ETL_DEFN a
INNER JOIN ORACLEDAC.W_ETL_DEFN_STEP b
ON (a.ROW_WID = b.ETL_DEFN_WID)
INNER JOIN ORACLEDAC.W_ETL_STEP c
ON (b.STEP_WID = c.ROW_WID)
ORDER BY 
a.NAME 
, b.PRIORITY 
, c.NAME 
