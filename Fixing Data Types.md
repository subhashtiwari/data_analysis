Here we're taking about the data in image named Data Types. It contains the output of enrollment and data_engagement.
Every value in there is a string, but 'days_to_cancel' looks like logically it should be an integer. 
Cancel date is clearly a date and 'is cancelled' looks like a boolean, but they are representative strings. That's because the CSV library doesn't try to detect what type each column has. It's upto us if we want to convert tthese data types. 

