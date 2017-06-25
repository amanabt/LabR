#! /usr/bin/env python3

import sqlite3
import copy

class Material:
	'''
	'''
	
	def __init__(self):
		'''
		'''
		self._material = str()
		self._notes    = str()
		
		return
	pass

class Observation:
	'''
	'''
	
	def __init__(self):
		'''
		'''
		self._data   = []
		self._images = []
		self._videos = []
		
		return
	
	pass

class Procedure_step:
	'''
	'''
	
	def __init__(self):
		'''
		'''
		self._step        = str()
		self._observation = []
		self._cautions    = []
		
		return
	
	pass


class LabR:
	'''
	'''
	
	def __init__(self):
		'''
		'''
		
		#Declaration of the variables.
		
		self._start_time    = None
		self._end_time      = None
		self._project_title = str()
		self._purpose       = []
		self._materials     = []
		self._theory        = str()
		self._procedures    = str()
		
		return
	
	def addProjectTitle(self, project_title):
		'''
		'''
		self._project_title = project_title
		return

	def add_purpose(self, purpose):
		'''
		'''
		self._purpose.append(purpose)
		return
	
	def add_material(self, material):
		'''
		'''
		self._materials.append(material)
		return
	
	def add_theory(self, theory):
		'''
		'''
		self._theory = theory
		return
	
	
	pass

if __name__ == '__main__':
	'''
	'''
	
	labr1 = LabR()
	
	labr1.addProjectTitle(input('Enter Project Title:'))
	labr1.add_purpose(input('Enter Purpose:'))
	
	return

