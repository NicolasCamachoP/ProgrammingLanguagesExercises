class DFA: #AFD
    def __init__(self):
        self.states = set({})
        self.transitions = {}
    #end def constructor


    def add_state(self, q):
        self.states.add(q)
    #end def

    def add_transitions(self, q1, symbol, q2):
        self.transitions[(q1, symbol)] = q2
    #end def

    def process_string(self, string, finalState):
        q = next(iter(self.states))
        for i in string:
            q = self.transitions.get((q,i))
            if (q == None): break
        #end for
        return  q in finalState
    #end def
        
    #end def

    def __repr__(self):
        return "Q = " + str(self.states) + "\nδ = " + str(self.transitions)
    #end def

if __name__ == "__main__":
    dfa = DFA()

    #Alphabet list initialize 
    alpha_list = [] 
    aux = 'a'
    for i in range(0, 26): 
        alpha_list.append(aux) 
        aux = chr(ord(aux) + 1)
    #end for
    aux = 'A'
    for i in range(26, 52): 
        alpha_list.append(aux) 
        aux = chr(ord(aux) + 1)
    #end for

    #Creating all the states
    dfa.add_state(0)
    dfa.add_state(1)
    dfa.add_state(2)
    dfa.add_state(3)
    dfa.add_state(4)
    dfa.add_state(5)

    #Creating transitions for letters
    for i in range (0,52):
        dfa.add_transitions(0,alpha_list[i],1)
        dfa.add_transitions(1,alpha_list[i],1)
        dfa.add_transitions(2,alpha_list[i],3)
        dfa.add_transitions(3,alpha_list[i],3)
        dfa.add_transitions(4,alpha_list[i],5)
        dfa.add_transitions(5,alpha_list[i],5)
    #end for

    #Creating dot (".") transitions
    dfa.add_transitions(3,".",4)
    dfa.add_transitions(5,".",4)

    #Creating at ("@") transitions
    dfa.add_transitions(1,"@",2)

    #Test AFD
    string = "h@h.b"
    if (dfa.process_string(string, [5])):
        print(f"The adress mail formed by {string} is correct!")
    else:
        print(f"The adress mail formed by {string} is not correct!")
    string = "hola@hotmail..com"
    if (dfa.process_string(string, [5])):
        print(f"The adress mail formed by {string} is correct!")
    else:
        print(f"The adress mail formed by {string} is not correct!")
    string = "nicolasCamacho@javeriana.edu.co"
    if (dfa.process_string(string, [5])):
        print(f"The adress mail formed by {string} is correct!")
    else:
        print(f"The adress mail formed by {string} is not correct!")