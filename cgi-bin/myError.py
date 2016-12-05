#!/usr/local/bin/python3
# coding: utf-8

class DBError(Exception):
	def __str__(self):
		return "Unexpected error related DB."
