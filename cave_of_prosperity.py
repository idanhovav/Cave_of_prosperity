""" A great problem I tried to solve in Java and failed miserably
at. Let's try it again with my newfound CS skills!
Link to prompt: 
https://www.reddit.com/r/dailyprogrammer/comments/3aewlg/20150617_challenge_219_
hard_the_cave_of_prosperity/


"""

import os.path

def choose(cap, weight, pieces, chosen=[]):
	"""	Returns the pieces chosen for the highest total that is still
	less than the capacity.

	"""
	if len(pieces) == 0:
		return chosen
	elif weight == cap:
		return chosen
	elif weight + pieces[0] > cap:
		return choose(cap, weight, pieces[1:], chosen)
	else:
		a = choose(cap, weight + pieces[0], pieces[1:],
					  chosen + list(pieces[0]))
		b = choose(cap, weight, pieces[1:], chosen)
		if sum(a) >= sum(b):
			return a
		return b



def make_int(x):
	""" Since we're working with 7 digit floating points
	we can change to ints and then save space?

	"""
	return x * (10 ** 7)

def make_float(x):
	return x / (10 ** 7)


if __name__ == "__main__":
	response = input("File Name? ")
	source = open(response, 'r')
	cap = make_int(eval(source.readline()) )
	nuggets = eval(source.readline())
	pieces = []
	for x in range(nuggets):
		pieces.append(make_int(eval(source.readline())))
	chosen = map(make_float, choose(cap, 0, pieces))
	a = 1
	name = "output" + str(a)
	while os.path.exists(name):
		a += 1
		name = "output" + str(a)
	out = open(name, 'w')
	out.write(str(sum(chosen)))
	for x in chosen:
		out.write(str(x))
	out.close()





