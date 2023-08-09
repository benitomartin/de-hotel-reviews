{{ config(materialized='table') }}



with review_data as 
(
  select *
    from {{ ref('stg_hotel_reviews') }}

)


select
    review_data.hotelid,
    review_data.hotel_name, 
    review_data.hotel_country,
    review_data.review_date,
    review_data.reviewer_score,
    review_data.average_score,
    review_data.hotel_rating,
    review_data.reviewer_nationality

    
from review_data