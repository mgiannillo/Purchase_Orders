
---- A look at Purchase Order volume by vendor ----
SELECT Vendor,
COUNT(PO_Number) AS PO_Count
FROM po_data..PO_Data
GROUP BY Vendor
ORDER BY PO_Count DESC

---- A look at Purchase Order volume by Spend Type ----
SELECT Type_of_Spend,
FORMAT(SUM(CAST(PO_Amount AS INT)), 'C') AS Total_Spending
FROM po_data..PO_Data
GROUP BY Type_of_Spend
ORDER BY Total_Spending DESC

---- Spending by Brand and Spend Category ----
SELECT Brand, Type_of_Spend, 
FORMAT(SUM(CAST(PO_Amount AS INT)), 'C') AS Comittment,
FORMAT(SUM(CAST(Invoice_Amount AS INT)), 'C') AS Actual,
FORMAT(SUM(CAST(Difference AS INT)), 'C') AS Unpaid,
COUNT(PO_Number) AS PO_Count
FROM po_data..PO_Data
GROUP BY Brand, Type_of_Spend
ORDER BY Brand, Type_of_Spend

---- A look at total Purchase Order spending by vendor ----
SELECT Vendor,
FORMAT(SUM(CAST(PO_Amount AS INT)), 'C') AS Total_PO_Spending,
Brand
FROM po_data..PO_Data
GROUP BY Vendor, Brand
ORDER BY Vendor

---- Make Column for Q1-Q4 and look at spending throughout the year ----

SELECT 
Period,
Month,
FORMAT(SUM(CAST(PO_Amount AS INT)), 'C') AS Total_PO_Spending
FROM (SELECT 
*,
CASE 
	WHEN Date_Opened BETWEEN '01/01/2022' AND '03/31/2022' THEN 'Q1'
	WHEN Date_Opened BETWEEN '04/01/2022' AND '06/30/2022' THEN 'Q2'
	WHEN Date_Opened BETWEEN '07/01/2022' AND '09/30/2022' THEN 'Q3'
	WHEN Date_Opened BETWEEN '10/01/2022' AND '12/31/2022' THEN 'Q4'
	ELSE 'NA'
END AS Period,
SUBSTRING(CAST(Date_Opened AS VARCHAR), 6, 2) AS Month
FROM po_data..PO_Data) AS case_table
GROUP BY Month, Period
ORDER BY Month, Total_PO_Spending 

---- Totals ----
SELECT
FORMAT(SUM(CAST(PO_Amount AS INT)), 'C') AS Committed_YTD,
FORMAT(SUM(CAST(Invoice_Amount AS INT)), 'C') AS Invoiced_YTD,
FORMAT(SUM(CAST(Difference AS INT)), 'C') AS Difference
FROM po_data..PO_Data


















