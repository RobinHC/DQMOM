#! /usr/bin/env python

from dolfin import *
from numpy import *
import distribution_diffusion as mod

def main():

    # some constants
    T = 5.0
    dt = 0.1
    dim = 2
    n_ele = 20
    N = 2
    A_cond = 1e-11
    A_pert = 1e-3
    D_x = 1e-3
    G = 1.0
    minField = 1e-6
    abscissa_0 = [Expression('0.4*floor(x[0]+0.45)' + 
                             '+ 0.9*(1-ceil(x[0]-0.45))' +
                             '0.0')]#'+ pow(minField,0.5)', minField=minField), 
                  Expression('0.6*floor(x[0]+0.45)' + 
                             '+ 1.1*(1-ceil(x[0]-0.45))' +
                             '0.0')]#'+ pow(minField,0.5)', minField=minField)]
    weight_0 = [Expression('0.5*floor(x[0]+0.45)' + 
                           '+ 0.5*(1-ceil(x[0]-0.45))' +
                           '+ minField', minField=minField), 
                Expression('0.5*floor(x[0]+0.45)' + 
                           '+ 0.5*(1-ceil(x[0]-0.45))' +
                           '+ minField', minField=minField)]

    # Create files for storing solution    
    files_a = [File("results_2/weight_" + str(i) + ".pvd") for i in range(N)]   
    files_b = [File("results_2/abscissa_" + str(i) + ".pvd") for i in range(N)]
    files_c = [File("results_2/weighted_abscissa_" + str(i) + ".pvd") for i in range(N)]
    files_d = [File("results_2/density.pvd"),File("results_2/mean.pvd"),File("results_2/std_dev.pvd")]
    files = files_a + files_b + files_c + files_d

    # import pdb; pdb.set_trace()

    mod.main(T, dt, dim, n_ele, N, A_cond, A_pert, D_x, abscissa_0, weight_0, files)

main()
