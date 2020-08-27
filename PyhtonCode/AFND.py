class AFND: #AFD
    def __init__(self):
        self.states = set({})
        self.transitions = {}
    #end def constructor


    def add_state(self, q):
        self.states.add(q)
    #end def

    def add_transitions(self, q1, symbol, q):
        self.transitions[(q1, symbol)] = q
    #end def
    
    def recurrentTravel(self, index, state, finalState, string):        
        #Chek if the actual state is the final state
        if index >= len(string): return state in finalState
        #checking for childs
        isValid = False
        qs = self.transitions.get((state, string[index]))
        if qs != None:
            for i in qs:
                isValid = self.recurrentTravel(index + 1, i, finalState, string)
                if (isValid): return True
            #end for
        #end if
        #Checking for "e" transitions
        qs = self.transitions.get((state, 'e'))
        if qs != None:
            for i in qs:
                isValid = self.recurrentTravel(index, i, finalState, string)
                if (isValid): return True
        #end for
        return False
    #end def

    def process_string(self, string, finalState):
        return self.recurrentTravel(0,next(iter(afnd.states)),finalState, string)
    #end def

    def __repr__(self):
        return "Q = " + str(self.states) + "\nδ = " + str(self.transitions)
    #end def

if __name__ == "__main__":
    afnd = AFND()

    #Creating all the states
    afnd.add_state(1)
    afnd.add_state(2)
    afnd.add_state(3)
    afnd.add_state(4)

    #Adding transitions
    afnd.add_transitions(1,"1",[1,2])
    afnd.add_transitions(1,"0",[1])
    afnd.add_transitions(2,"0",[3])
    afnd.add_transitions(2,"e",[3])
    afnd.add_transitions(3,"1",[4])
    afnd.add_transitions(4,"0",[4])
    afnd.add_transitions(4,"1",[4])
    
    #Test afnd
    string = "00101"
    if (afnd.process_string(string, [4])):
        print(f"The input {string} has been accepted!")
    else:
        print(f"The input {string} has not been accepted!")
    string = "0011"
    if (afnd.process_string(string, [4])):
        print(f"The input {string} has been accepted!")
    else:
        print(f"The input {string} has not been accepted!")
    string = "11101"
    if (afnd.process_string(string, [4])):
        print(f"The input {string} has been accepted!")
    else:
        print(f"The input {string} has not been accepted!")
    string = "010110"
    if (afnd.process_string(string, [4])):
        print(f"The input {string} has been accepted!")
    else:
        print(f"The input {string} has not been accepted!")