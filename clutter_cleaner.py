import os
files=os.listdir("Cluttered folder")
i=1
for file in files:
    if file.endswith(".avif"):
        print(file)
        os.rename(f"Cluttered folder/{file}",f"Cluttered folder/{i}.png")
        i=i+1