for engagement_record in daily_engagement:
    engagement_record['account_key'] = engagement_record['acct']
    del[engagement_record['acct']]

# In here we have modified the list rather creat a new list. We looped over the 'daily_engagement' table
# And for each row first created a new key, account key and set it equal to the existing values stored under the key 'acct'.
# Then once the value had been copied, we delete the 'acct' key from hte dictionary. It doesn't have any output.

