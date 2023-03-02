
---- Tableau Query "Total Spending VS. Forecast" ----
SELECT 
Period,
FORMAT(SUM(PO_Amount), 'C') AS Total_PO_Spending
FROM (SELECT 
*,
CASE 
	WHEN Date_Opened BETWEEN '01/01/2022' AND '03/31/2022' THEN 'Q1'
	WHEN Date_Opened BETWEEN '04/01/2022' AND '06/30/2022' THEN 'Q2'
	WHEN Date_Opened BETWEEN '07/01/2022' AND '09/30/2022' THEN 'Q3'
	WHEN Date_Opened BETWEEN '10/01/2022' AND '12/31/2022' THEN 'Q4'
	ELSE 'NA'
END AS Period
FROM po_data..PO_Data) AS case_table
GROUP BY  Period
ORDER BY Total_PO_Spending 

---- Tableau Query "Distribution of Spending by Category ----

SELECT Type_of_Spend,
FORMAT(SUM(PO_Amount), 'C') AS Total_Spending
FROM po_data..PO_Data
GROUP BY Type_of_Spend
ORDER BY Total_Spending DESC

--- Tableau Query "Total Spending by Brand ----

SELECT Brand,
FORMAT(SUM(PO_Amount), 'C') AS Total_Spending
FROM po_data..PO_Data
GROUP BY Brand
ORDER BY Total_Spending DESC

---- Tableau Query "Spend Type Totals by Brand" ----

SELECT Brand, Type_of_Spend, 
FORMAT(SUM(PO_Amount), 'C') AS Comittment
FROM po_data..PO_Data
GROUP BY Brand, Type_of_Spend
ORDER BY Brand, Type_of_Spend

