import math
import pydot
graph=pydot.Dot(graph_type='digraph')

class State():
	def __init__(self, cannibalLeft, missionaryLeft, boat, cannibalRight, missionaryRight, game):
		self.cannibalLeft = cannibalLeft
		self.missionaryLeft = missionaryLeft
		self.boat = boat
		self.cannibalRight = cannibalRight
		self.missionaryRight = missionaryRight
		self.parent=None
		self.game=game

	def is_goal(self):
		if self.cannibalLeft == 0 and self.missionaryLeft == 0:
			return True
		else:
			return False

	def is_valid(self):
		if  (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) \
                   and (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight):
			return True
		else:
			return False

	def iss_valid(self):
		if (self.missionaryLeft >= 0 and self.missionaryRight >= 0 and self.cannibalLeft >= 0 and self.cannibalRight >= 0):
			return True
		else:
			return False

	def __eq__(self, other):
		return self.cannibalLeft == other.cannibalLeft and self.missionaryLeft == other.missionaryLeft \
                   and self.boat == other.boat and self.cannibalRight == other.cannibalRight \
                   and self.missionaryRight == other.missionaryRight

	def __hash__(self):
		return hash((self.cannibalLeft, self.missionaryLeft, self.boat, self.cannibalRight, self.missionaryRight, self.game))

def successors(cur_state):
		children = [];
		if cur_state.boat == 'left':
			new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft - 2, 'right',
	                                  cur_state.cannibalRight, cur_state.missionaryRight + 2, None)
			## Two missionaries cross left to right.
			if new_state.is_valid()==False:
				new_state.game="over"

			if new_state.iss_valid():
				new_state.parent=cur_state
				children.append(new_state)

			new_state = State(cur_state.cannibalLeft - 2, cur_state.missionaryLeft, 'right',
	                                  cur_state.cannibalRight + 2, cur_state.missionaryRight, None)
			## Two cannibals cross left to right.
			if new_state.is_valid()==False:
				new_state.game="over"

			if new_state.iss_valid():
				new_state.parent=cur_state
				children.append(new_state)

			new_state = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft - 1, 'right',
	                                  cur_state.cannibalRight + 1, cur_state.missionaryRight + 1, None)
			## One missionary and one cannibal cross left to right.

			if new_state.is_valid()==False:
				new_state.game="over"

			if new_state.iss_valid():
				new_state.parent=cur_state
				children.append(new_state)

			new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft - 1, 'right',
	                                  cur_state.cannibalRight, cur_state.missionaryRight + 1, None)
			## One missionary crosses left to right.

			if new_state.is_valid()==False:
				new_state.game="over"

			if new_state.iss_valid():
				new_state.parent=cur_state
				children.append(new_state)


			new_state = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft, 'right',
	                                  cur_state.cannibalRight + 1, cur_state.missionaryRight, None)
			## One cannibal crosses left to right.

			if new_state.is_valid()==False:
				new_state.game="over"

			if new_state.iss_valid():
				new_state.parent=cur_state
				children.append(new_state)

		else:
			new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft + 2, 'left',
	                                  cur_state.cannibalRight, cur_state.missionaryRight - 2, None)
			## Two missionaries cross right to left.

			if new_state.is_valid()==False:
				new_state.game="over"

			if new_state.iss_valid():
				new_state.parent=cur_state
				children.append(new_state)

			new_state = State(cur_state.cannibalLeft + 2, cur_state.missionaryLeft, 'left',
	                                  cur_state.cannibalRight - 2, cur_state.missionaryRight, None)
									  ## Two cannibals cross right to left.

			if new_state.is_valid()==False:
				new_state.game="over"


			if new_state.iss_valid():
				new_state.parent=cur_state
				children.append(new_state)

			new_state = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft + 1, 'left',
	                                  cur_state.cannibalRight - 1, cur_state.missionaryRight - 1, None)
			## One missionary and one cannibal cross right to left.

			if new_state.is_valid()==False:
				new_state.game="over"


			if new_state.iss_valid():
				new_state.parent=cur_state
				children.append(new_state)

			new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft + 1, 'left',
	                                  cur_state.cannibalRight, cur_state.missionaryRight - 1, None)
			## One missionary crosses right to left.

			if new_state.is_valid()==False:
				new_state.game="over"

			if new_state.iss_valid():
				new_state.parent=cur_state
				children.append(new_state)


			new_state = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft, 'left',
	                                  cur_state.cannibalRight - 1, cur_state.missionaryRight, None)
			## One cannibal crosses right to left.
			if new_state.is_valid()==False:
				new_state.game="over"

			if new_state.iss_valid():
				new_state.parent=cur_state
				children.append(new_state)

		return children




def breadth_first_search():
		initial_state = State(3,3,'left',0,0, None)
		goal_state=State(0,0,'right',3,3, None)
		c=0
		frontier = list()
		explored = set()
		frontier.append(initial_state)
		while frontier:
			state = frontier.pop(0)
			if (state.game!="over") and (state not in explored):
				children = successors(state)
				explored.add(state)
				for child in children:
					c=c+1
					if child in explored:
						child.game="over"

					if (child not in explored):
						if child==goal_state:
							goal_node=pydot.Node("0,0,right,3,3,WIN", style='filled', fillcolor='green')
							graph.add_node(goal_node)
							node_d=pydot.Node(str(child.parent.missionaryLeft)+","+str(child.parent.cannibalLeft)+","+str(child.parent.boat)+","+str(child.parent.missionaryRight)+","+str(child.parent.cannibalRight)+","+str(child.parent.game), style='filled', fillcolor='white')
							graph.add_edge(pydot.Edge(node_d,goal_node))
							break
						if child.game == "over":
							node_a=pydot.Node(str(child.missionaryLeft)+","+str(child.cannibalLeft)+","+str(child.boat)+","+str(child.missionaryRight)+","+str(child.cannibalRight)+","+str(child.game), style='filled', fillcolor='yellow')
							node_b=pydot.Node(str(child.parent.missionaryLeft)+","+str(child.parent.cannibalLeft)+","+str(child.parent.boat)+","+str(child.parent.missionaryRight)+","+str(child.parent.cannibalRight)+","+str(child.parent.game), style='filled', fillcolor='yellow')
						else:
							node_a=pydot.Node(str(child.missionaryLeft)+","+str(child.cannibalLeft)+","+str(child.boat)+","+str(child.missionaryRight)+","+str(child.cannibalRight)+","+str(child.game), style='filled', fillcolor='green')
							node_b=pydot.Node(str(child.parent.missionaryLeft)+","+str(child.parent.cannibalLeft)+","+str(child.parent.boat)+","+str(child.parent.missionaryRight)+","+str(child.parent.cannibalRight)+","+str(child.parent.game), style='filled', fillcolor='green')
						graph.add_node(node_a)
						graph.add_edge(pydot.Edge(node_b,node_a))
						frontier.append(child)


		print('total states %d' %c)
		graph.write_png('example.png')



def main():
	breadth_first_search()


main()
