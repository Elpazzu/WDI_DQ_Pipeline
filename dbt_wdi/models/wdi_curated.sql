{{ config(materialized='table') }}

SELECT *
FROM {{ source('wdi', 'wdi_data') }}
WHERE "Country_Code" IS NOT NULL 
  AND "Country_Name" IS NOT NULL