import os
import shutil
from hashlib import md5
# Source path
source ="projects/challenge/New Dir/newww.txt"

# Destination path
destination = "projects/challenge"
print("source : ",source,"\n destination : ",destination)

# shutil.copy(source,destination)
dest="/projects/challenge/newww.txt"

# Print path of newly
# created file
print("Destination path:", dest)


with open('.hidden.txt','w') as outfile:
	outfile.write(dest)



