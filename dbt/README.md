Create Schema in BQ (pur region europe-west6 in the query): `dbt_hotels_all`  and add this as Dataset while creaing the project in dbt. By running the dbt run, the table will be saved here

Give a project name and put the same name under models in dbt_project.yml


dbt run --select stg_hotel_reviews

Add the macro in the macros folder and in the stg_hotel_reviews

Install the packages.yml running dbt deps

Create a unique key with:

    {{ dbt_utils.generate_surrogate_key(['hotel_address', 'hotel_name']) }} as hotelid,


Add the variable

-- dbt build --m <model.sql> --var 'is_test_run: false'
{% if var('is_test_run', default=true) %}

-- Limit the result to 100 rows
limit 100

{% endif %}

And run

dbt run --models stg_hotel_reviews --vars '{"is_test_run": false}'
