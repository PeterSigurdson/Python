select repair_id as "repair customer id", cellphone as, charge , bike_id 

from repair_data

where NOT EXISTS

(  
SELECT purchase_records.purchase_id 

from purchase_records

where purchase_records.cellphone = repair_data.cellphone 


  );