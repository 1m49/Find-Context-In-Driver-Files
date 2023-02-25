
import glob

# set filepath to search
# path = '/Users/imanakbari/ml_guides/' + '**/*.ipynb'
# first part : file src | second part : extension files
path = 'E:/' + '**/*.py'

# string to search for
search_term = 'def numeric():'

# empty list to hold files that contain matching string
files_to_check = []

# looping through all the filenames returned
# set recursive = True to look in sub-directories too
for filename in glob.iglob(path, recursive=True):
    # adding error handling just in case!
    try:
        with open(filename) as f:
            # read the file as a string
            contents = f.read()
            # if the search term is found append to the list of files
            if search_term in contents:
                files_to_check.append(filename)
    except:
        print('there isn\'t any context ')

print('---------------------------------')

print('result : \n',files_to_check,'\n' ,end='\n')

print('---------------------------------')
