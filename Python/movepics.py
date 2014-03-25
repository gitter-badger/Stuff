import os

dir = os.getcwd()+"/";
todir = dir+"Bilder/"
try:
	os.mkdir(todir)
except OSError:
	print "Directory exists"
print dir, todir
for file in os.listdir(dir):
	filel=file.lower()
	if filel.endswith(".jpg") or filel.endswith(".png") or filel.endswith(".gif"):
		try:
			print dir+file
			os.rename(dir+file,todir+file)
		except OSError:
			print "Error: "+file