{{ config(materialized='view') }}


-- Select Relevant Columns
select
    Hotel_Address as hotel_address,
    cast(Review_Date as timestamp) as review_date,
    cast(Average_Score as float64) as average_score,
    {{ get_hotel_rating_description("Average_Score") }} as hotel_rating,
    Hotel_Name as hotel_name,
    Reviewer_Nationality as reviewer_nationality,
    Negative_Review as negative_review,
    cast(Total_Number_of_Reviews as integer) as total_number_of_reviews,
    Positive_Review as positive_review,
    cast(Total_Number_of_Reviews_Reviewer_Has_Given as integer) as total_number_of_reviews_reviewer_has_given,
    cast(Reviewer_Score as float64) as reviewer_score,
    Tags as tags

from {{ source('staging', 'hotel_reviews') }}

limit 100