import numpy as np
from qiskit import *
from qiskit import Aer 

def backend_name():

    circ = QuantumCircuit(3)
    # Run the quantum circuit on a statevector simulator backend
    backend = Aer.get_backend('statevector_simulator')
    #print(backend.name())
    return backend.name()
    