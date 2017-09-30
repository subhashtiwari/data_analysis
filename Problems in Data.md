There are some problems in the data, they are discussed below.

1. There are more unique students in the enrollment table than in the engagement table. The engagement table is supposed  to include a row for each day that each student is enrolled, even if the students didn't visit he site at all that day.
So there should have been the same number of unique students in both table.

2. The column containing student account keys was named 'account_key' in two of the tables and 'acct' in the third. This one isn't a big problem but it is inconvenient. It can be easy to forget which table has 'account_key' and which one has 'acct'.

To fix the second problem is easier than first one. We can change the column name from 'acct' to 'account_key' by removin value for 'acct' in each row and adding it back under the name 'account_key'. 

Now we have to write the code to fix this problem.

To fix the first problem that is why some students are missing from daily_engagement.
It's important to investigate things like this. If we don't know why something's happening in our data, we could be missing something important in our analysis and we can't really trust your results. 

To investigate these problems we can use a process, it is described below.
1. First we need to identify which specific data points are surprising. 
In our case that would be any enrollment record with no corresponding engagement data. 

2. Print out one or a few of the surprising data points. Sometimes we can tell just by looking what the problem is. 

Now we fix this problem.

We won't always see the problem at first glance so more investigation may be necessary. Often we will find a problem just by looking at some of the surprising points, or we might find that there aactually wasn't even a problem in the first place.
Such as in one place a student had cancelled within one day of joining, and that's not really a problem, and it does explain why that student was missing from the engagement table. 
We might like to exclude students like this or might just need to know these students exist in case they cause an edge case in code. 

At this point the process repeats itself, once again we need to identify any remaining surprising data points, if any. And then fix them.

To find any more surprising records left we write a program to check the number of suprising record left.