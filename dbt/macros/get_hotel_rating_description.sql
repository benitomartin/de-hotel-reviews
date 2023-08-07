 {#
    This macro returns the description of the hotel_rating 
#}


{% macro get_hotel_rating_description(Average_Score) -%}
    case
        when {{ Average_Score }} >= 9 then 'Superb: 9+'
        when {{ Average_Score }} >= 8 then 'Very good: 8+'
        when {{ Average_Score }} >= 7 then 'Good: 7+'
        when {{ Average_Score }} >= 6 then 'Pleasant: 6+'
        when {{ Average_Score }} >= 5 then 'Below average: 5+'
    end
{% endmacro %}



