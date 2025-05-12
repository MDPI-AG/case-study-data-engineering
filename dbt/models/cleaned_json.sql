with raw as (
    select * from {{ source('raw', 'raw_json_data') }}
)

-- select from fields
select 
    reference-count,
    publisher,
    license,
    short-container-title,
    published-print,
    DOI,
    type,
    is-referenced-by-count,
    title,
    container-title,
    references-count,
    URL,
    ISSN,
    issn-type,
    published,
    published-online,
    abstract,
    update-policy,
    language
from raw