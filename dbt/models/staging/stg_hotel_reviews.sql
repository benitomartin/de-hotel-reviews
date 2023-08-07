{{ config(materialized='view') }}


-- Select Relevant Columns
select
    -- identifiers 
        -- Generate a surrogate key (unique identifier) for the hotel using hotel_address and hotel_name
    {{ dbt_utils.generate_surrogate_key(['hotel_address', 'hotel_name']) }} as hotelid,
    Hotel_Address as hotel_address,
    Hotel_Name as hotel_name,

    -- Convert to timestamps
    cast(Review_Date as timestamp) as review_date,

    -- Scoring information
    cast(Reviewer_Score as float64) as reviewer_score,
    cast(Average_Score as float64) as average_score,
    {{ get_hotel_rating_description("Average_Score") }} as hotel_rating,

    -- Review Type
    Negative_Review as negative_review,
    Positive_Review as positive_review,
    cast(Total_Number_of_Reviews as integer) as total_number_of_reviews,
    
    -- Reviewer information
    Reviewer_Nationality as reviewer_nationality,
    cast(Total_Number_of_Reviews_Reviewer_Has_Given as integer) as total_number_of_reviews_reviewer_has_given,
    Tags as tags

from {{ source('staging', 'hotel_reviews') }}
where hotel_name is not null 

-- dbt build --m <model.sql> --var 'is_test_run: false'
{% if var('is_test_run', default=true) %}

-- Limit the result to 100 rows
limit 100

{% endif %}