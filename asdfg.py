import numpy as np
from scipy.linalg import eigh
import matplotlib.pyplot as plt


# Define the operators (normalised prefactors)
SI = np.eye(3, dtype=np.complex128)
SX = (np.sqrt(1/2) *
      np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=np.complex128))
SY = (-1j * np.sqrt(1/2) *
      np.array([[0, 1, 0], [-1, 0, 1], [0, -1, 0]], dtype=np.complex128))
SZ = (
      np.array([[1, 0, 0], [0, 0, 0], [0, 0, -1]], dtype=np.complex128))


def tensor(op_list):
    """Finds tensor product of a list of operators."""
    # Initialise product as a 1x1 I matrix
    product = np.eye(1, dtype=np.complex128)
    for op in op_list:
        product = np.kron(product, op)
    return product


def aklt(n, closed=True, costheta=1., sintheta=1./3):
    """Returns the energy spectrum of a spin chain of N spins.
    N: number of spins in the chain
    closed: is the spin chain periodic or not (represents a change in topology)
    costheta, sintheta: can be used to set the biquadratic coupling constant"""

    # Calculate sx, sy and sx operators for all positions in the chain
    # E.g for the 2nd spin on a 4 spin chain: I.Sx.I.I

    sx_list = []
    sy_list = []
    sz_list = []

    # For each position in the chain
    for j in range(n):
        # Initialise list of identity matrices
        op_list = [SI]*n

        # Replace jth identity matrix with Pauli x matrix
        op_list[j] = SX
        # Calculate tensor product of all matrices in the list
        sx_list.append(tensor(op_list))

        # Repeat for other Pauli matrices
        op_list[j] = SY
        sy_list.append(tensor(op_list))

        op_list[j] = SZ
        sz_list.append(tensor(op_list))

    # Initialise Hamiltonian
    h = 0

    # Sum each spin's contribution to the Hamiltonian
    for j in range(n if closed else n-1):
        # Get the index of j and j+1, returning to 0 at j=n+1
        a, b = j, (j+1) % n

        s_dot_s = 0  # Initialise S_j.S_j+1

        s_dot_s += np.dot(sx_list[a], sx_list[b])
        s_dot_s += np.dot(sy_list[a], sy_list[b])
        s_dot_s += np.dot(sz_list[a], sz_list[b])

        h += (1./2) * s_dot_s + (1./6) * np.dot(s_dot_s, s_dot_s) + (1./3) * np.eye(s_dot_s.shape[0])


    return np.sort(eigh(h)[0])

def L_dependecy():
    aklt2 = aklt(2)
    #aklt4 = aklt(4)
    #aklt6 = aklt(6)
    L2 = np.arange(0,9)
    L4 = np.arange(0,len(aklt4))
    L6 = np.arange(0, len(aklt6))
    aklt2o = aklt(2, False)
    aklt4o = aklt(4, False)
    aklt6o = aklt(6, False)
    #aklt7=aklt(7)
    #print(aklt6)
    #print(aklt7)
    plt.figure(0)
    plt.plot(L2,aklt2, label="L=2")
    #plt.plot(L4,aklt4, label="L=4")
    #plt.plot(L6, aklt6, label="L=6")
    plt.legend()
    plt.xlabel("Energy level")
    plt.ylabel("E")
    plt.title("Energy values for closed chain")
    #plt.figure(1)
    #plt.plot(L2, aklt2o, label="L=2")
    #plt.plot(L4, aklt4o, label="L=4")
    #plt.plot(L6, aklt6o, label="L=6")
    #plt.xlabel("Energy level")
    #plt.ylabel("E")
    #plt.title("Energy values for open chain")
    #plt.legend()

    #plt.legend()
    #plt.show()

def open_vs_closed():

    # Print the lowest 10 energy levels for closed chain
    aklt_closed = aklt(4)
    print("Closed chain:")
    print(np.round(aklt_closed[:10], 2))

    # Print the lowest 10 energy levels for open chain
    aklt_open = aklt(4, False)
    print("Open chain:")
    print(np.round(aklt_open[:10], 2))

    # Plot energy spectra
    fig, ax = plt.subplots()

    ax.plot(aklt_closed[:10], 'ks--', label='Closed')
    ax.plot(aklt_open[:10], 'ko:', mfc='white', label='Open')

    ax.set_ylabel("Energy")
    ax.set_xlabel("Level Index")
    ax.legend()




if __name__ == '__main__':
    #open_vs_closed()
    L_dependecy()
