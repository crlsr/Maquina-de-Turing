class MaquinaTuring:
    def __init__(self, tape: list, transition_table, label, head_position=0):
        self.tape = tape
        self.head_position = head_position
        self.blank_symbol = "0"
        self.transition_table = {}
        for instruction in transition_table:
            key = (instruction[0], instruction[1])
            value = (instruction[2], instruction[3], instruction[4])
            self.transition_table[key] = value
        self.current_state = transition_table[0][0]
        self.final_states = {transition_table[-1][0]}
        self.label = label
        

    def step(self):
        
        symbol_under_head = self.tape[self.head_position]
        current_state_symbol_pair = (self.current_state, symbol_under_head)
    
        if current_state_symbol_pair in self.transition_table:
            new_state, new_symbol, head_movement = self.transition_table[current_state_symbol_pair]
            self.tape[self.head_position] = new_symbol
            newLabel = ''.join(str(self.tape)).replace("[", "").replace("]", "")

            self.label.configure(text = newLabel, font= ("Century Gothic", 20.5, )) 
            print (str(self.tape))
            print(newLabel)

            self.set_head_position(self.head_position + head_movement)
            print(f"Head movement: {head_movement}")

            self.label.place(x = 105 - 20 * self.head_position, y=60)

            self.current_state = new_state
            self.label.after(500)
            
            if self.current_state in self.final_states:
                print("Se alcanzó un estado final, se detiene la animación.")
                print(self.tape)
                return

        newLabel = ''.join(str(self.tape)).replace("[", "").replace("]", "")
        self.label.configure(text = newLabel, font= ("Century Gothic", 20.5, )) 
        self.label.after(500, self.step)

    def final(self):
        return self.current_state in self.final_states

    def set_head_position(self, int):
        if int > len(self.tape):
            return
        if int < 2:
            if int == 0:
                self.tape.insert(0, 0)
                self.tape.insert(0, 0)
            elif int == 1:
                self.tape.insert(0, 0)
            self.head_position = 2

        elif int >= len(self.tape) - 2:
            if int == len(self.tape) - 1:
                self.tape.append(0)
            elif int == len(self.tape) - 2:
                self.tape.append(0)
                self.tape.append(0)
            self.head_position = len(self.tape) - 3
        
        else:
            self.head_position = int
            
    def run(self):
        self.step()
       
        