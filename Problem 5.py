# Here we check if there is/are any more surprising data still in the enrollment data. That are the number of problem students.

num_problem_students = 0            'Here we have initialised the problem students as zero'
for enrollment in enrollments:          'This loop checks each account key inthe enrollement table and checks wheter that account key was present in the daily engagement table.'
    student = enrollment['account_key']
    if (student not in unique_engagement_students and                   'This checks whether the join date is equal to the cancel date'
            enrollment)['joindate'] != enrollment['cancel_date']):
        print enrollment
        num_problem_students += 1                               'THen if there was a missing student for whom the two dates were not equal, we added one to the total number of probelm students.'

 num_problem_students                       'Here we printed the output.'

# We could also haev checked whether the days to cancel was equal to zero.

# The three problematic enrollments, were Udacity test accounts, as they all have is Udacity equal to True.
# After we remove these three test accounts there are no more surprising data left.