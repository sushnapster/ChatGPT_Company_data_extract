select * from chatgpt_company_research

delete from chatgpt_company_research

drop table chatgpt_company_research
CREATE TABLE public.chatgpt_company_research (
	chatgpt_company_research_id varchar,
	company_name varchar not NULL,
	what_to_search varchar not NULL,
	what_is_the_result text NULL,
	"comments" text NULL,
	result_extracted_date timestamptz NULL DEFAULT now(),
	result_updated_date timestamptz null,
	CONSTRAINT chatgpt_company_research_pkey PRIMARY KEY (chatgpt_company_research_id)
);