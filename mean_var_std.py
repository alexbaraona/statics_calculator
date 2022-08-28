import numpy as np
import math

def calculate(list):
  # check if all elements are numbers.
  try:
    numbers = [float(x) for x in list]
  except:
    raise ValueError("List must only contain numbers.")
    
  # if less then 9 elements, raise exceptions.
  flattened_data = np.array(numbers)  
  if len(flattened_data) < 9:
    raise ValueError("List must contain nine numbers.")
    
  # list must have a square number of elements in order to create a square matrix.
  int_root = math.isqrt(len(flattened_data))
  if int_root != math.sqrt(len(flattened_data)):
    raise ValueError("List must have a square number of elements.")
  matrix_data = np.reshape(flattened_data, (int_root,int_root))
  
  # calculate each value and use list comprehention to help format data
  mean = [np.mean(matrix_data, axis = x).tolist() for x in [0,1,None]]
  variance = [np.var(matrix_data, axis = x).tolist() for x in [0,1,None]]
  standard_deviation = [np.std(matrix_data, axis = x).tolist() for x in [0,1,None]]
  max = [np.max(matrix_data, axis = x).tolist() for x in [0,1,None]]
  min = [np.min(matrix_data, axis = x).tolist() for x in [0,1,None]]
  sum = [np.sum(matrix_data, axis = x).tolist() for x in [0,1,None]]
    
  return {
    'mean': mean,
    'variance': variance,
    'standard deviation': standard_deviation,
    'max': max,
    'min': min,
    'sum': sum
  }