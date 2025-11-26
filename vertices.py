# Main rotor base vertices
main_prop_vertices = [
    -0.3, -0.003,
     0.3, -0.003,
     0.3,  0.003,

    -0.3, -0.003,
     0.3,  0.003,
    -0.3,  0.003
]

# Rear blade vertices
rear_blade_vertices = [
    -0.06, -0.005,
     0.06, -0.005,
     0.06,  0.005,

    -0.06, -0.005,
     0.06,  0.005,
    -0.06,  0.005
]

# Helicopter vertices
heli_vertices = [
    
    # Body
    -0.10, -0.10,   # dowm left
     0.15, -0.10,   # down right
    -0.10,  0.10,   # up left

     0.15, -0.10,   # down right
    -0.10,  0.10,   # up left
     0.15,  0.10,   # up right

    # Tail
     0.15,  0.10,   # up left
     0.15,  0.00,   # down left
     0.65,  0.13,   # up right 
        
    # Undertail
     0.15,  0.00,   # up left
     0.15, -0.10,   # down left
     0.20,  0.02,   # up right
        
    # Nose
    -0.10,  0.10,   # up  left
    -0.20,  0.00,   # down left
    -0.10,  0.00,   # down right
        
    -0.15, -0.10,   # down  left
    -0.10, -0.10,   # down right
    -0.10,  0.00,   # up right
    
    # Main Rotor
     0.03,  0.10,   # down left
     0.05,  0.10,   # down right
     0.05,  0.13,   # up right
    
     0.03,  0.10,   # down left
     0.05,  0.13,   # up right
     0.03,  0.13,   # up left
    
    # Landing skids
    # Left leg
    -0.06, -0.10,   # up left
    -0.06, -0.13,   # down left
    -0.05, -0.13,   # down right
    
    -0.06, -0.10,   # up left
    -0.05, -0.13,   # down right
    -0.05, -0.10,   # up right
    
    # Right leg
     0.10, -0.10,   # up left
     0.10, -0.13,   # down left
     0.11, -0.13,   # down right

     0.10, -0.10,   # up left
     0.11, -0.13,   # down right
     0.11, -0.10,   # up right
    
    # Horizontal bar
    -0.12, -0.13,   # up left
    -0.12, -0.135,  # down left
     0.17, -0.135,  # down right
        
    -0.12, -0.13,   # up left
     0.17, -0.135,  # down right
     0.17, -0.13,   # up right
]