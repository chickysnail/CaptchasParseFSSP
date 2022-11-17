import hashlib
import os

# where to take captchas from
dirPath = "Captchas10000"
# where to save hashes
savePath = r'captchas_hashes10000.txt'

hashSet = set()
for filename in os.listdir(dirPath):
    with open(os.path.join(dirPath, filename), 'rb') as file:
        image = file.read()
        hash = hashlib.sha256(image).hexdigest()
        hashSet.add(hash)

print(f"There are {len(hashSet)} unique captchas")

with open(savePath, 'w') as fp:
    for item in hashSet:
        # write each item on a new line
        fp.write("%s\n" % item)
    print('Done')
