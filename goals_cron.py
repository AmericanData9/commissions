from src.db_connector import *
from datetime import datetime, timedelta


####---- GET CLOSE DATE ----####
today = datetime.now()

yesterday = today - timedelta(days=1)
close_date = yesterday.strftime("%m_%Y")
close_date = str(close_date)

####---- GET MONTH AND YEAR ----####
close_date_month = yesterday.strftime("%m")
close_date_month = str(close_date_month)
close_date_year = yesterday.strftime("%Y")
close_date_year = str(close_date_year)
print(close_date_month)


####---- CREATION OF THE MATERIALIZED VIEW QUERY FROM THE NORMAL VIEW CALLED: all_contracts_items_goals ----####
all_contracts_materialized_view = f"""CREATE MATERIALIZED VIEW all_contracts_items_goals_mview_{close_date}
AS SELECT * FROM goals_all_contracts_items WHERE signature_month={close_date_month} AND signature_year={close_date_year} WITH DATA;"""

####---- CREATION OF THE MATERIALIZED VIEW QUERY FROM THE NORMAL VIEW CALLED: goal_sales ----####
goals_materialized_view = f"""CREATE MATERIALIZED VIEW goals_sales_mview_{close_date}
AS SELECT * FROM goal_sales 
WHERE signature_month={close_date_month} AND signature_year={close_date_year} WITH DATA;"""

####---- REFRESH MATERIALIZED VIEW CALLED: all_contracts_items_goals_mview{close_date} ----####
refresh_all_contracts_items_goals_mview_query = f"""REFRESH MATERIALIZED VIEW all_contracts_items_goals_mview{close_date};"""

####---- REFRESH MATERIALIZED VIEW CALLED: goal_sales_mview{close_date} ----####
refresh_goal_sales_mview_query = f"""REFRESH MATERIALIZED VIEW goal_sales_mview{close_date};"""

push_query(all_contracts_materialized_view)
push_query(goals_materialized_view)
# push_query(refresh_all_contracts_items_goals_mview_query)
# push_query(refresh_goal_sales_mview_query)