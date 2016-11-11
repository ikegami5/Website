#!/usr/bin/env python3
# coding: utf-8
import sys

def main():
	print("Hello, Python!")
	version = list(sys.version_info)[0:3]
	print("version: {0[0]}.{0[1]}.{0[2]}".format(version))

if __name__ == "__main__":
	main()

