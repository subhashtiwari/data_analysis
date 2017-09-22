
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

In Python the contents of a CSV file are commonly rpresented as a list of rows. 
There are two common choices for how to represent each row. 
In the first option, each row is a list. So, then the overall data structure is a list of lists. 

In the second option, each row is a dictionary. This option works well if you have a CSV header because then the keys of each dictionary can be column names and the fields can be values. So then the overall data structure would be alist of dictionaries. 
Now we could write code to read in the data from the CSV ourself and it wouldn't be too hard, there aer libraries already written to do it. 

In the image named Code a code is written using Python unicodecsv library toread in the student enrollments and print out the first record. 
The code in the image is taken directly from the example code on the CSV model documentation page.

In tihs code first created the list of enrollment, then open the file. 
The mode 'rb' here means that the file will be opened for reading. And teh 'b' flag changes the format of how the file is read.
The CSV documentation page mentions that we have to use this when we use this library.
DictReader is also used in it, it means that each row will be a dictionary. It is used because the data have a header row and it will allow to refer each column by its name rather than its number.
Now the reader won't actually be a list of row, it will be called an iterator. The iterator lets us write a for loop to access each element, but only once.
If we add a second loop to print out all the row in hte reader, then actually nothing would be printed, because we can only loop over an iterator once. So, we used my one loop to append each row to a list. And finally we need to close the file. 
The enrollment is the last row in the cell, it gets the output in the output area. 

This code is a bit ike lengthier than it needs to be in a couple of ways.
1. We could have avoid having to close the file by instead using a with statement. 
When we open a file using a with statement we need to indent everything that accesses that file. Then once the indented blockends, the file will automatically be closed.

2. There's actually an easier way to convert an iterator to a list. We've created a list of the enrollment data without using a loop. So there is no need for the for loop. 

The simplified code is shown in image named Simple Code.

