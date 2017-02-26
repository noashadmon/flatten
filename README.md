# flatten
Programming challenge for Button

If iPython notebook is installed on machine, download the flatten.ipynb file and run through the code. 
Otherwise, the .py is included as well. 
To run the '.py' file first download it. Then make sure you have python 2.7 installed on your machine. In the command line run "python flatten.py". This will run the flatten script as well as print the output to some test cases as well. 

Explanation of program:
The flatten method I constructed is a recursive function. First it checks to see if the input list is iterable. This just means that the object is capable of returning its members one at a time. If it is, then we continue onto the next element (which can be a sublist/list of lists) of the list and flatten it as well. We continue to do this until we've reached the end of the list and then return a list of the flattened sublists. If our input is not iterable, then we just return a list of the element.

This could have also been done using the collections class in python. The only part that would have been changed is instead of using hasattr(l, "__iter__") we would say isinstance(l, collections.Iterable). However, importing a separate library can be slow (not necessarily in this case) so decided against it. Lastly, the only way I can see my program breaking is if the user inputs something that isn't valid like an uninitialized variable. However, the error that would be returned would be because the variable is not initialized, not because the flatten method doesn't work. 
