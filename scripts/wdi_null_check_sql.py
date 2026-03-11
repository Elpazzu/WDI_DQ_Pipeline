import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

with psycopg2.connect(
    host='localhost', port=5433, dbname='wdi_db',
    user='postgres', password='mypassword123'
) as conn:
    with conn.cursor() as cur:
        # Total rows
        cur.execute("SELECT COUNT(*) FROM public.wdi_data")
        total = cur.fetchone()[0]
        
        # Country Name nulls
        cur.execute("SELECT COUNT(*) FROM public.wdi_data WHERE \"Country Name\" IS NULL OR \"Country Name\" = ''")
        country_name_nulls = cur.fetchone()[0]
        country_name_complete = 100 * (1 - country_name_nulls / total)
        print(f'✅ "Country Name": {country_name_nulls} empty/null ({country_name_complete:.2f}% complete)')
        
        # Country Code nulls
        cur.execute("SELECT COUNT(*) FROM public.wdi_data WHERE \"Country Code\" IS NULL OR \"Country Code\" = ''")
        country_code_nulls = cur.fetchone()[0]
        country_code_complete = 100 * (1 - country_code_nulls / total)
        print(f'✅ "Country Code": {country_code_nulls} empty/null ({country_code_complete:.2f}% complete)')

print("All checks passed!" if country_name_nulls == 0 and country_code_nulls == 0 else "Failures found!")