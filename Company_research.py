'''
Created by Sushant
Date: 18 Feb 2023
Comments: To fetch company details
'''
#import python frameworks
import openai
import argparse
import psycopg2
#start time
from datetime import datetime
start_time = datetime.now()
import time
print(start_time)

##177 db connection
conn = psycopg2.connect(database=db_name, user=user, password=pwd, host=ip, port=port, keepalives=99999999, keepalives_idle=99999999, keepalives_interval=10, keepalives_count=15)

#command line arguents
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("company_name", help="Argument 1 : Company name")
    args = parser.parse_args()

company_name_0 =str(args.company_name)
company_name_1 =str(args.company_name)
company_name_1 =  ("'{}'".format(company_name_1))

print ('Provided Company name is ------------> ',company_name_0)
print('********************************************************************************************** ')

# Set up the OpenAI API client
openai.api_key = "API_KEY"

# Set up the model and prompt
model_engine = "text-davinci-003"

################### 1 ############################################################3
prompt = 'What products or services does '+str(company_name_0)+' provide?'
print('Question:',prompt)

# Generate a response
completion1 = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=200,
    n=1,
    stop=None,
    temperature=0.5,
)

response1 = completion1.choices[0].text
#print(response1)
#print(f"Company_Name: {company_name_1} | prompt: {prompt} | Result: {response1}")

###load into DB
concat = company_name_0+'|'+prompt
concat =  ("'{}'".format(concat))
prompt =  ("'{}'".format(prompt))
response1 = response1.strip()
response1 = response1.replace("'", '"')
response1 =  ("'{}'".format(response1))


cursor = conn.cursor()
a = conn.cursor()
a.execute('''
         insert into public.chatgpt_company_research (chatgpt_company_research_id,company_name, what_to_search, what_is_the_result)
            values ('''+str(concat)+''','''+str(company_name_1)+''','''+str(prompt)+''',trim('''+str(response1)+'''))
        ''')
conn.commit()

################### 2 ###########################################################3

prompt = 'Where is '+str(company_name_0)+' located and where do they operate?'
print('Question:',prompt)

# Generate a response
completion2 = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=200,
    n=1,
    stop=None,
    temperature=0.5,
)

response2 = completion2.choices[0].text
#print(response2)

###load into DB
concat = company_name_0+'|'+prompt
concat =  ("'{}'".format(concat))

prompt =  ("'{}'".format(prompt))
response2 = response2.strip()
response2 = response2.replace("'", '"')
response2 =  ("'{}'".format(response2))

cursor = conn.cursor()
b = conn.cursor()
b.execute('''
         insert into public.chatgpt_company_research (chatgpt_company_research_id,company_name, what_to_search, what_is_the_result)
            values ('''+str(concat)+''','''+str(company_name_1)+''','''+str(prompt)+''',trim('''+str(response2)+'''))
        ''')
conn.commit()

######################## 3 #######################################################3

prompt = 'What is '+str(company_name_0)+' ownership structure?'
print('Question:',prompt)

# Generate a response
completion3 = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=200,
    n=1,
    stop=None,
    temperature=0.5,
)

response3 = completion3.choices[0].text
#print(response3)

###load into DB
concat = company_name_0+'|'+prompt
concat =  ("'{}'".format(concat))

prompt =  ("'{}'".format(prompt))
response3 = response3.strip()
response3 = response3.replace("'", '"')
response3 =  ("'{}'".format(response3))

cursor = conn.cursor()
c = conn.cursor()
c.execute('''
         insert into public.chatgpt_company_research (chatgpt_company_research_id,company_name, what_to_search, what_is_the_result)
            values ('''+str(concat)+''','''+str(company_name_1)+''','''+str(prompt)+''',trim('''+str(response3)+'''))
        ''')
conn.commit()

######################## 4 #######################################################3

prompt = 'What is '+str(company_name_0)+' financial performance, including revenue, net income, and growth over time?'
#print('Question:',prompt)

# Generate a response
completion4 = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=200,
    n=1,
    stop=None,
    temperature=0.5,
)

response4 = completion4.choices[0].text
#print(response4)

###load into DB
concat = company_name_0+'|'+prompt
concat =  ("'{}'".format(concat))

prompt =  ("'{}'".format(prompt))
response4 = response4.strip()
response4 = response4.replace("'", '"')
response4 =  ("'{}'".format(response4))

cursor = conn.cursor()
d = conn.cursor()
d.execute('''
         insert into public.chatgpt_company_research (chatgpt_company_research_id,company_name, what_to_search, what_is_the_result)
            values ('''+str(concat)+''','''+str(company_name_1)+''','''+str(prompt)+''',trim('''+str(response4)+'''))
        ''')
conn.commit()

######################## 5 #######################################################3

prompt = 'What is '+str(company_name_0)+' reputation in the market, including customer reviews, industry awards, and recognition?'
print('Question:',prompt)

# Generate a response
completion5 = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=200,
    n=1,
    stop=None,
    temperature=0.5,
)

response5 = completion5.choices[0].text
#print(response5)

###load into DB
concat = company_name_0+'|'+prompt
concat =  ("'{}'".format(concat))

prompt =  ("'{}'".format(prompt))
response5 = response5.strip()
response5 = response5.replace("'", '"')
response5 =  ("'{}'".format(response5))

cursor = conn.cursor()
e = conn.cursor()
e.execute('''
         insert into public.chatgpt_company_research (chatgpt_company_research_id,company_name, what_to_search, what_is_the_result)
            values ('''+str(concat)+''','''+str(company_name_1)+''','''+str(prompt)+''',trim('''+str(response5)+'''))
        ''')
conn.commit()

######################## 6 #######################################################3

prompt = 'Who are '+str(company_name_0)+' key competitors, and how does '+str(company_name_0)+' compare to them in terms of market share and financial performance?'
print('Question:',prompt)

###load into DB
concat = company_name_0+'|'+prompt
concat =  ("'{}'".format(concat))
completion6 = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=200,
    n=1,
    stop=None,
    temperature=0.5,
)

response6 = completion6.choices[0].text
#print(response6)

###load into DB
concat = company_name_0+'|'+prompt
concat =  ("'{}'".format(concat))

prompt =  ("'{}'".format(prompt))
response6 = response6.strip()
response6 = response6.replace("'", '"')
response6 =  ("'{}'".format(response6))

cursor = conn.cursor()
f = conn.cursor()
f.execute('''
         insert into public.chatgpt_company_research (chatgpt_company_research_id,company_name, what_to_search, what_is_the_result)
            values ('''+str(concat)+''','''+str(company_name_1)+''','''+str(prompt)+''',trim('''+str(response6)+'''))
        ''')
conn.commit()

######################## 7 #######################################################3

prompt = 'can you please share '+str(company_name_0)+' research reports?'
print('Question:',prompt)

# Generate a response
completion7 = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=200,
    n=1,
    stop=None,
    temperature=0.5,
)

response7 = completion7.choices[0].text
#print(response7)

###load into DB
concat = company_name_0+'|'+prompt
concat =  ("'{}'".format(concat))

prompt =  ("'{}'".format(prompt))
response7 = response7.strip()
response7 = response7.replace("'", '"')
response7 =  ("'{}'".format(response7))

cursor = conn.cursor()
g = conn.cursor()
g.execute('''
         insert into public.chatgpt_company_research (chatgpt_company_research_id,company_name, what_to_search, what_is_the_result)
            values ('''+str(concat)+''','''+str(company_name_1)+''','''+str(prompt)+''',trim('''+str(response7)+'''))
        ''')
conn.commit()

######################## 8 #######################################################3

prompt = 'what is '+str(company_name_0)+' supply chain report?'
print('Question:',prompt)

# Generate a response
completion8 = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=200,
    n=1,
    stop=None,
    temperature=0.5,
)

response8 = completion8.choices[0].text
#print(response8)

###load into DB
concat = company_name_0+'|'+prompt
concat =  ("'{}'".format(concat))

prompt =  ("'{}'".format(prompt))
response8 = response8.strip()
response8 = response8.replace("'", '"')
response8 =  ("'{}'".format(response8))

cursor = conn.cursor()
h = conn.cursor()
h.execute('''
         insert into public.chatgpt_company_research (chatgpt_company_research_id,company_name, what_to_search, what_is_the_result)
            values ('''+str(concat)+''','''+str(company_name_1)+''','''+str(prompt)+''',trim('''+str(response8)+'''))
        ''')
conn.commit()

######################## 9 #######################################################3

prompt = 'What is '+str(company_name_0)+' supply chain risk problems?'
print('Question:',prompt)

# Generate a response
completion9 = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=200,
    n=1,
    stop=None,
    temperature=0.5,
)

response9 = completion9.choices[0].text
#print(response9)

###load into DB
concat = company_name_0+'|'+prompt
concat =  ("'{}'".format(concat))

prompt =  ("'{}'".format(prompt))
response9 = response9.strip()
response9 = response9.replace("'", '"')
response9 =  ("'{}'".format(response9))

cursor = conn.cursor()
i = conn.cursor()
i.execute('''
         insert into public.chatgpt_company_research (chatgpt_company_research_id,company_name, what_to_search, what_is_the_result)
            values ('''+str(concat)+''','''+str(company_name_1)+''','''+str(prompt)+''',trim('''+str(response9)+'''))
        ''')
conn.commit()

######################## 10 #######################################################3

prompt = 'what all '+str(company_name_0)+' subsidiary companies?'
print('Question:',prompt)

# Generate a response
completion10 = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=200,
    n=1,
    stop=None,
    temperature=0.5,
)

response10 = completion10.choices[0].text
#print(response10)

###load into DB
concat = company_name_0+'|'+prompt
concat =  ("'{}'".format(concat))

prompt =  ("'{}'".format(prompt))
response10 = response10.strip()
response10 = response10.replace("'", '"')
response10 =  ("'{}'".format(response10))

cursor = conn.cursor()
j = conn.cursor()
j.execute('''
         insert into public.chatgpt_company_research (chatgpt_company_research_id,company_name, what_to_search, what_is_the_result)
            values ('''+str(concat)+''','''+str(company_name_1)+''','''+str(prompt)+''',trim('''+str(response10)+'''))
        ''')
conn.commit()

###conn close
conn.close()
print(' ')
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
print(end_time)