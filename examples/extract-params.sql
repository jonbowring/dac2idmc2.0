-- Export the task parameters
SELECT 
p.row_wid as "param_wid"
,p.name AS "name"
,p.value AS "value"
,p.type_cd AS "type_cd"
,p.step_wid AS "step_wid"
,p.DATATYPE AS "datatype"
,p.CONTEXT_TYPE AS "context_type"
,p.INACTIVE_FLG AS "inactive_flag"
,p.comments AS "comments"
FROM 
ORACLEDAC.W_ETL_PARAM p

-- Export the execution parameters
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

/*
======================================================
Exploration queries below this line
======================================================
*/

-- Extracting parameter values
-- Note: One parameter can be split across many rows. They all share the same obj_wid, order them using sequence, and use the pointer ptr_next to move to the next value

SELECT
row_wid AS "row_wid",
obj_wid AS "obj_wid",
last_upd AS "last_upd",
textfield AS "textfield",
sequence AS "sequence",
obj_type AS "obj_type",
ptr_next AS "ptr_next",
version_id AS "version_id"
FROM
ORACLEDAC.w_etl_text
--WHERE
--obj_wid = '9231AACC755C751FD26BEB513C23225'
ORDER BY
obj_wid,
sequence;

-- Source system parameters
SELECT 
ROW_WID
, NAME AS "name"
, VALUE AS "value"
, DEF_VALUE as "def_value"
, DATATYPE AS "datatype"
, TYPE_CD AS "type_cd"
, DB_TYPE as "db_type"
, STEP_WID AS "step_wid"
, APP_WID as "source_system_container"
, EP_WID as "ep_wid"
, CONTEXT_TYPE AS "context_type"
, LAST_UPD as "last_upd"
, INACTIVE_FLG AS "inactive_flag"
, COMMENTS AS "comments"
, VERSION_ID AS "version_id"
FROM
w_etl_param p
WHERE
type_cd = 'Informatica parameters'
ORDER BY
name;

-- Task Parameters for an Execution Plan
SELECT 
a.ROW_WID AS "plan_wid",
a.name AS "plan_name",
b.ROW_WID AS "plan_step_wid",
c.ROW_WID AS "step_wid",
c.name AS "step_name",
p.ROW_WID AS "param_wid",
p.APP_WID AS "source_system_container",
p.name AS "param_name",
p.value AS "param_value",
p.def_value AS "param_def_value"
FROM 
ORACLEDAC.W_ETL_DEFN a
INNER JOIN ORACLEDAC.W_ETL_DEFN_STEP b
ON (a.ROW_WID = b.ETL_DEFN_WID)
INNER JOIN ORACLEDAC.W_ETL_STEP c
ON (b.STEP_WID = c.ROW_WID)
INNER JOIN ORACLEDAC.w_etl_param p
ON (c.row_wid = p.step_wid)
WHERE
a.name = 'Echo Employee Snapshot Oracle R12.1.3';

-- Connectivity parameters for an execution plan
SELECT 
a.name,
b.row_wid,
b.etl_defn_wid, --execution plan id
b.name,
b.value,
b.copy_num,
b.src_delay,
b.type_cd,
b.prune_days, --value IS IN minutes. E.g. 2,880 = 2 days
b.app_wid,
b.last_upd,
b.inactive_flg,
b.comments,
b.version_id
FROM 
ORACLEDAC.W_ETL_DEFN a
INNER JOIN ORACLEDAC.w_etl_defn_prm b
ON (a.row_wid = b.etl_defn_wid)
WHERE
a.name = 'Echo Employee Snapshot Oracle R12.1.3';

-- Execution parameters for an Execution Plan
SELECT 
a.name AS "plan_name",
p.*
FROM 
ORACLEDAC.W_ETL_DEFN a
INNER JOIN ORACLEDAC.w_etl_defn_oprm p
ON (a.row_wid = p.etl_defn_wid)
WHERE
a.name = 'Echo Employee Snapshot Oracle R12.1.3';