-- Export the execution parameters "params-exec.csv"
SELECT 
p.ROW_WID AS "param_wid"
,p.name AS "name"
,p.etl_defn_wid as "plan_wid"
,'Execution parameters' AS "type_cd"
,p.DATATYPE AS "datatype"
,p.CONTEXT_TYPE AS "context_type"
,p.INACTIVE_FLG AS "inactive_flag"
,p.comments AS "comments"
FROM 
ORACLEDAC.w_etl_defn_oprm p;