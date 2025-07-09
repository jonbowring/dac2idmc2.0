/*
SELECT * FROM ORACLEDAC.W_ETL_DEFN;
SELECT distinct TYPE_CD FROM ORACLEDAC.W_ETL_DEFN_STEP;
SELECT * FROM ORACLEDAC.W_ETL_STEP;
SELECT * FROM ORACLEDAC.W_ETL_SYSPROP;
SELECT * FROM ORACLEDAC.W_ETL_SERVER;
*/

/*
-- Possible parameter inputs
SELECT * FROM ORACLEDAC.W_ETL_DEFN_TBL; -- Not 100% certain on this one
SELECT * FROM ORACLEDAC.W_ETL_DEFN_PRM;
SELECT * FROM ORACLEDAC.W_ETL_PARAM;

-- Execution plans have both "Connectivity parameters" and "Execution parameters" inputs
 * 
 */

/*
-- Index recreation
-- Possible DB types DB2, DB2-390, MSSQL, ORACLE, TERADATA, NETEZZA, TIMESTEN
SELECT * FROM ORACLEDAC.W_ETL_INDEX;
SELECT * FROM ORACLEDAC.W_ETL_INDEX_COL;
SELECT * FROM ORACLEDAC.W_ETL_TABLE;
 */

WITH normalised AS (
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
),

task_params AS (
	
	SELECT 
	p.name AS "name",
	p.value AS "value",
	p.type_cd AS "type_cd",
	p.step_wid AS "step_wid",
	p.DATATYPE AS "datatype",
	p.CONTEXT_TYPE AS "context_type",
	p.INACTIVE_FLG AS "inactive_flag",
	p.comments AS "comments"
	FROM 
	ORACLEDAC.W_ETL_PARAM p
	--inner JOIN ORACLEDAC.W_ETL_STEP S ON (p.STEP_WID = s.ROW_WID)
	
)




--SELECT type_cd, count(1) FROM task_params GROUP BY type_cd ORDER BY 2 DESC

--SELECT * FROM task_params where type_cd = 'Informatica parameters' 
--AND value IS NOT NULL 

--SELECT * FROM task_params where type_cd = 'Folder' 

--SELECT * FROM task_params

--SELECT * FROM normalised WHERE plan_name = 'Echo Employee Snapshot Oracle R12.1.3'


SELECT
p.*
FROM
task_params p
INNER JOIN (
	SELECT * FROM normalised WHERE plan_name = 'Echo Employee Snapshot Oracle R12.1.3'
) t
ON (p.STEP_WID = t.STEP_WID)

/*
SELECT 
*
FROM 
normalised
WHERE 
plan_name = 'Echo Employee Snapshot Oracle R12.1.3';
*/

/*
SELECT 
a.plan_name,
count(1)
FROM 
normalised a
GROUP BY
a.plan_name
ORDER BY 
2
;
*/