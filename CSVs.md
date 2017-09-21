
We've acquired the data by downloading the files that were available. In other cases we might need to get data from an API or might need to scrape it from a web page. 
We often need to combine data from multiple different formats.

The files that are downloaded are in a format called CSV which stands for Comma Seperated Values. 
A CSV file is similar to a spreadsheet with no formulas. 
The CSV format is also very easy to process using code, unlike XLSX file which is format used by Microsort Excel.

For example a file containing student enrollments, in a Google Spreadsheeets, there is a row for each time a student enrolls and columns for different pieces of information such as the account key, the enrollment date and the cancellation date, if any. 

If this same file is open in a plain text editor it will look like shown in image named File.
A plain text editor is a program like Notepad or Sublime that shows exactly what is present in the file. 
In the image it is shown that the actual contents of the file are very simple. 
The header row from the spreadsheet is present as the first line of CSV file. The second row of the spreadsheet is the second line of teh CSV and so on.

Within each row, you'll see the first cell, followed by a comma, followed by a second cell, followed by a comma. this makes CSv's very easy to process in programming such as Python.

# CSV in Python

In Python the contents of a CSV file are commonly rpresented as a list of rows. There are two common choices for how to represent each row. In the first option, each row is a list. 
So, then the overall data structure is a list of lists. In the second option, each row is a dictionary. This option works well if you have a CSV header because then the keys of each dictionary can be column names and the fields can be values. 
So then the overall data structure would be alist of dictionaries. Now we could write code to read in the data from the CSV ourself and it wouldn't be too hard, there aer libraries already written to do it. 