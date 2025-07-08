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
	a.ROW_WID AS PLAN_WID
	, a.NAME AS PLAN_NAME
	, a.INACTIVE_FLG AS PLAN_INACTIVE_FLAG
	, b.ROW_WID AS PLAN_STEP_WID
	, b.PRIORITY AS PLAN_STEP_ORDER
	, b.TYPE_CD AS PLAN_STEP_TYPE
	, c.ROW_WID AS STEP_WID
	, c.CMD_NAME AS STEP_CMD
	, c.NAME AS STEP_NAME
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
	p.name,
	p.value,
	p.type_cd,
	p.step_wid,
	p.DATATYPE,
	p.CONTEXT_TYPE,
	p.INACTIVE_FLG,
	p.comments
	--,
	--p.version
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