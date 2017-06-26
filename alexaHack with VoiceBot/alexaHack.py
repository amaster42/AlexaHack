import sys
import subprocess

logpath = 'C:\\tools\\logs'
errlog = logpath + "\\error.log"
outputlog = logpath + "\\output.log"
cmdlog = logpath + "\\cmd.log"
pathToNmap = "C:\\tools\\nmap\\nmap "

def main(event):
	if event=='default': run("-sS 127.0.0.1")
	if event=='mark': run("evilbotnet.com")
	if event=='advscan': run("-A 127.0.0.1")

def run(cmd):
	l = open(errlog,"w")
	o = open(outputlog,"w")
	c = open(cmdlog,"w")
	
	c2 = pathToNmap + cmd
	print c2
	subprocess.call(c2)
	#c2.write(cmd2 + "\n")

	l.close()
	o.close()
	c.close()

if __name__ == "__main__":
	main(sys.argv[1])
