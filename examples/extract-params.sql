SELECT 
p.name AS "name"
,p.value AS "value"
,p.type_cd AS "type_cd"
,p.step_wid AS "step_wid"
,p.DATATYPE AS "datatype"
,p.CONTEXT_TYPE AS "context_type"
,p.INACTIVE_FLG AS "inactive_flag"
,p.comments AS "comments"
FROM 
ORACLEDAC.W_ETL_PARAM p