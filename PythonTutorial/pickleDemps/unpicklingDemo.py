
import os
import builtins
import pickle
import sys

sys.tracebacklimit = 0
import traceback
import io
from logging import Logger
import pickle

safe_builtins = [
		'range',
		'complex',
		'set',
		'frozenset',
	
	]

class RestrictedUnpickler(pickle.Unpickler):

   def find_class(self, module, name):
    # Only allow safe classes from builtins.
      if module == "builtins" and name in safe_builtins:
	      return getattr(builtins, name)
	# Forbid everything else.
      raise pickle.UnpicklingError("global '%s.%s' is forbidden" %
      (module, name))

def restricted_loads(s):
	return RestrictedUnpickler(io.BytesIO(s)).load()


k=[3, 4, 5, 6, 7, 8, 9];
# print(restricted_loads(pickle.dumps(k[slice(0,8,3)])))
#
# print(restricted_loads(pickle.loads(b"cos\nsystem\n(S'echo hello everyone'\ntR.")))


def func1(a):
	try:
		x = restricted_loads(pickle.dumps(a))
		return x
	except pickle.UnpicklingError:
		s = traceback.format_exc()

		return s


def func2(s):
	try:
		x = restricted_loads(pickle.dumps([s,slice(0,8,3)]))
		return s[x]
	except pickle.UnpicklingError:
		s=traceback.format_exc()
		return s


if __name__ == "__main__":
	a = 50
	b = func1(a)
	print(b)
	y = tuple(input())
	z = func2(y)
	print(z)