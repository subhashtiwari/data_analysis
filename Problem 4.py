# This code is to fix the problems 

for enrollment in enrollments:
    student = enrollment['account_key']
    if student not in unique_engagement_students:
        print enrollment
        break

# We found out that the join_date and cancel_date are the same and the days_to_cancel is equal to zero.
# This explains why there is no record in the engagement table for a full day before their engagement is recorded.
# In order to find this record, we looped over the enrollment table and found the account key for each enrollment.
# Then we checked whetther that account key was in the set of unique students in the engagement table. 
# If the student was missing from the engaegment table, then print the record and then breaak to exit the loop. 