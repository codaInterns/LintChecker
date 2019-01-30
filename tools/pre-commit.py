#!/usr/bin/env python3
import os
import subprocess
import sys
from glob import glob
def fun():	
	commitids = os.popen('git log --format="%H" -n 2').read()
	commitids = commitids.splitlines()
	diff = os.popen('git diff --name-only ' + commitids[0] + ' ' + commitids[1]).read()
	diff = diff.splitlines()
	basepath = sys.argv[1]
	basepath += '\\'
	isLintingProper = 1
	for i in diff:
		base=os.path.basename(i)
		if os.path.splitext(base)[1] == '.ts':
			cmd = os.popen('tslint '+basepath+i).read()
			if len(cmd) != 0:
				isLintingProper = 0
				sys.stderr.write(i)
				sys.stderr.write(cmd)
		elif os.path.splitext(base)[1] == '.java':
			# print(basepath+i)
			cmd = os.popen('java -jar ' + basepath+'tools\\java-linting-tools\\checkstyle-8.17-all.jar -c '+basepath + 'tools\\java-linting-tools\\sun_checks.xml ' + basepath+i).read()
			# print(cmd)
			# sys.stderr.write(str(len(cmd)))
			if len(cmd) != 0:
				isLintingProper = 0
				sys.stderr.write(basepath+i)
				sys.stderr.write(cmd)	


	return isLintingProper

if __name__ == "__main__":
	print(fun())
