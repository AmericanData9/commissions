from src.db_connector import *

query = """SELECT * FROM all_contracts_items
WHERE (EXTRACT(year FROM all_contracts_items.signature_date)) = 2023 AND diciembre > 0 AND contract_owner_name LIKE 'Silvia%'"""