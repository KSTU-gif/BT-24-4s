def nested_dict(n):
	if n == 0:
		return None
	return {'level' : n, 'next' : nested_dict(n-1)}
print(nested_dict(3))