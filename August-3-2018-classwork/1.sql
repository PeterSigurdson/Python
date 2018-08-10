SELECT cellphone, purchase_date, charge, bike_id, date_out INTO AAA
FROM (SELECT repair_data.cellphone, purchase_records.purchase_date, repair_data.charge, repair_data.bike_id, repair_data.date_out FROM repair_data LEFT JOIN purchase_records ON repair_data.cellphone = purchase_records.cellphone)  AS [%$##@_Alias];
