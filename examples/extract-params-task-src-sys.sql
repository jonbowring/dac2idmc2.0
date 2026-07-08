-- Export the task and source system parameters "params-task-src-sys.csv"
SELECT 
p.row_wid as "param_wid"
,p.name AS "name"
,p.value AS "value"
,p.type_cd AS "type_cd"
,p.step_wid AS "step_wid"
,p.app_wid as "source_system_container"
,p.DATATYPE AS "datatype"
,p.CONTEXT_TYPE AS "context_type"
,p.INACTIVE_FLG AS "inactive_flag"
,p.comments AS "comments"
FROM 
ORACLEDAC.W_ETL_PARAM p;