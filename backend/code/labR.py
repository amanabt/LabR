#! /usr/bin/env python3

import sqlite3
import copy
from datetime import datetime as dt
from datetime import timedelta

#[TODO] Implement auto-save function

class Material:
	'''
	'''
	
	def __init__(self, material = str()):
		'''
		'''
		self._material = material
		self._notes    = []
		
		return
	
	def add_material(self, material):
		'''
		'''
		self._material = material
		return
	
	def add_note(self, note):
		'''
		'''
		self._notes.append(note)
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

class Procedure:
	'''
	'''
	
	def __init__(self, step = None):
		'''
		'''
		self._step        = str()
		self._observation = []
		self._cautions    = []
		
		return
	
	def add_step(self, step):
		'''
		'''
		self._step = step
		
		return
	
	def add_observation(self, observation):
		'''
		'''
		self._observation.append(observation)
		return
	
	pass


class LabR:
	'''
	'''
	
	def __init__(self):
		'''
		'''
		#Declaration of the variables.
		
		self._start_time         = None
		self._end_time           = None
		self._time_of_experiment = None
		
		self._project_title = str()
		self._purpose       = []
		self._materials     = []
		self._theory        = str()
		self._procedures    = []
		
		return
	
	def start_experiment(self):
		'''
		'''
		self._start_time = dt.now()
		
		return
	
	def end_experiment(self):
		'''
		'''
		self._end_time = dt.now()
		self._time_of_experiment = self._start_time - self._end_time
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
	
	def add_theory(self, theory):
		'''
		'''
		self._theory = theory
		
		return
	
	def add_new_procedure(self, step = None):
		'''
		'''
		self._procedures.append(Procedure())
		
		return
	
	def addProcedureStep(self, procedure_idx, step):
		'''
		'''
		
		self._procedures[procedure_idx].add_step(step)
		return
	
	def addProcedureObservation(self, procedure_idx, observation):
		'''
		'''
		self._procedures[procedure_idx].add_observation(observation)
		return
	
	def recordImageObservation(self):
		'''
		'''
		print('Yet to be implemented!')
		return
	
	def recordData(self, procedure_idx):
		'''
		'''
		
		return
	
	def save(self):
		'''
		'''
		#[TODO]: Save the lab report.
		print('Yet to be implemented!')
		return
	
	pass

if __name__ == '__main__':
	'''
	'''
	
	labr1 = LabR()
	
	labr1.start_experiment()
	labr1.addProjectTitle(input('Enter Project Title: '))
	labr1.add_purpose(input('Enter Purpose: '))
	
	print('Press 1 to add material, to stop adding material, press 0: ')
	
	while(int(input()) == 1):
		material = Material(input('Enter Material Details: '))
		note     = input('Enter some note: ')
		material.add_note(note)
		
		labr1.add_material(material)
		pass
	
	print('Press 1 to add Procedure, to stop adding procedure, press 0: ')
	
	while(int(input()) == 1):
		step = input('Enter New step: ')
		labr1.add_new_procedure(step)
		
		pass
	pass


