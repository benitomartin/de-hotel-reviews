Create Schema in BQ (pur region europe-west6 in the query): `dbt_hotels_all`  and add this as Dataset while creaing the project in dbt. By running the dbt run, the table will be saved here

Give a project name and put the same name under models in dbt_project.yml


dbt run --select stg_hotel_reviews

