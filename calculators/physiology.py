import numpy as np

class Calculators():
    def __init__(self):
        pass


class Physiology(Calculators):
    def __init__(self):
        # self = super().__init()
        self.F = 96485 # C/Mole - Faradays Constant
        self.R = 8.314
        self.T = 37.7
        

    def charge(self, valence, moles):
        '''
        charge - calculates charge (q) using q=zFn
        '''
        return valence * self.F * moles # change (q)

    def current(self, charge, time): # C / s
        return charge / time 

    def electric_potential(self, charge, voltage):
        return charge * voltage

    def capacitance(self, charge, voltage):
        return charge / voltage

    def charge_from_capacitance(self, capacitance, voltage):
        return capacitance * voltage

    def n_moles(self, charge, valence):
        return charge / (valence * self.F)

    def flow(self, n_moles, time):
        return n_moles / time

    def flow_from_current(self, current, valence):
        return current / (valence * self.F)

    def flux_from_current(self, current, valence, area):
        return current / (valence * self.F * area)

    def ohms_law(self, voltage, resistance):
        return voltage / resistance


    def nernst(self, valence, conc_in, conc_out, temp=37.7, default=True):
        if default:
            return -(61 / valence) * np.log10(conc_in / conc_out)
        else:
            return -((self.R * temp) / (valence * self.F)) * np.log10(conc_in / conc_out)

    def goldman(self, conc_in, conc_out, permeability, valence=[1, 1, -1], default=True):
        conc_in, conc_out, permeability, valence = np.array(conc_in), np.array(conc_out), np.array(permeability), np.array(valence)
        if default:
            valence_mask = np.logical_not(valence > 0)
            # in_conc[valence_mask] = conc_out[valence_mask]
            # out_conc[valence_mask] = conc_in[valence_mask]


            print(valence_mask)
            print(permeability * conc_in)
            print(permeability * conc_out)
            return -61 * np.log10((permeability * conc_in) / (permeability * conc_out))
        
    
if __name__ == "__main__":
    calc = Physiology()
    nernst = calc.nernst(1, 140, 5)
    print(nernst)
    goldman = calc.goldman([10, 6, 140], [145, 106, 5], [0.02, 0.5, 1])
    print(goldman)
