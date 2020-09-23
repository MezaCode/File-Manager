# File-Manager
Personal windows file manager using python

it works by creating lists of key words to use to sort the files
each list belongs to a larger list. Like a tree. the leaf belongs to a branch. each leaf directory has a list of key words.
each directory that has sub directories will be a list of it's subdirs lists.

then we grab the file names and join their paths with os.path.join. this would be done in  a for each loop using os.walk

after that we begin the processes of sorting the files by checking to see from the largests lists (outer most directory) to the smallest list ( inner most directory)

once found for each level we then move on to the next level.
at the end we confirm that the file does exist and that it does not exist in the directory it will be moved to.
