import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# =====================================================================
#
# Function to read in outputs, combine them and sum them
#
# ---------------------------------------------------------------------
# 
# =====================================================================
def join_and_plot(OutDir, nSubs, nBoot, nReals, pVals):

	# Work out the number of sample sizes used
	nSampSizes = len(nSubs)

	# Work out number of p-values reported.
	nPvals = len(pVals)

	# Coverage table (we have a coverage result for each sample size
	# and p-value)
	covTable_est = np.zeros((nSampSizes,nPvals))
	covTable_true = np.zeros((nSampSizes,nPvals))

	# Coverage table (we have a coverage result for each sample size
	# and p-value) based on interpolated results
	covTable_est_intrp = np.zeros((nSampSizes,nPvals))
	covTable_true_intrp = np.zeros((nSampSizes,nPvals))

	# -----------------------------------------------------------------
	# For each sample size, read in the results
	# -----------------------------------------------------------------
	for i, nSub in enumerate(nSubs):

		# Read in observed values for the estimated boundary. This will be a 
		# boolean array of ones and zeros representing observed violations
		# across simulations
		obs_est = pd.read_csv(os.path.join(OutDir,'estSuccess'+str(nSub)+'.csv'), header=None, index_col=None)

		# Read in observed values for the true boundary. This will be a 
		# boolean array of ones and zeros representing observed violations
		# across simulations
		obs_true = pd.read_csv(os.path.join(OutDir,'trueSuccess'+str(nSub)+'.csv'), header=None, index_col=None)

		# Read in observed values for the estimated boundary. This will be a 
		# boolean array of ones and zeros representing observed violations
		# across simulations (based on interpolation assessment)
		obs_est_intrp = pd.read_csv(os.path.join(OutDir,'estSuccess'+str(nSub)+'_intrp.csv'), header=None, index_col=None)

		# Read in observed values for the true boundary. This will be a 
		# boolean array of ones and zeros representing observed violations
		# across simulations (based on interpolation assessment)
		obs_true_intrp = pd.read_csv(os.path.join(OutDir,'trueSuccess'+str(nSub)+'_intrp.csv'), header=None, index_col=None)

		# Get the coverage probabilities from the observed results for the
		# estimated boundary
		covTable_est[i,:] = np.mean(obs_est,axis=0)[:]

		# Get the coverage probabilities from the observed results for the
		# true boundary
		covTable_true[i,:] = np.mean(obs_true,axis=0)[:]

		# Get the coverage probabilities from the observed results for the
		# estimated boundary (for coverage assessed using interpolation)
		covTable_est_intrp[i,:] = np.mean(obs_est_intrp,axis=0)[:]

		# Get the coverage probabilities from the observed results for the
		# true boundary (for coverage assessed using interpolation)
		covTable_true_intrp[i,:] = np.mean(obs_true_intrp,axis=0)[:]

	# -----------------------------------------------------------------
	# For p-value, make a coverage plot
	# -----------------------------------------------------------------
	# Loop through p values making plots
	for i, p in enumerate(pVals):

		# Plot coverage for estimated along true boundary
	    #plt.plot(nSubs,covTable_true[:,i],color="red",label="True boundary")

	    # Plot coverage for estimated along estimated boundary
	    #plt.plot(nSubs,covTable_est[:,i],color="blue",label="Estimated boundary")

		# Plot coverage for estimated along true boundary (Interpolated)
	    plt.plot(nSubs,covTable_true_intrp[:,i],linestyle='dashed',color="red",label="True boundary (Interpolated)")

	    # Plot coverage for estimated along estimated boundary (Interpolated)
	    plt.plot(nSubs,covTable_est_intrp[:,i],linestyle='dashed',color="blue",label="Estimated boundary (Interpolated)")

	    # Line at p
	    plt.hlines(p, np.min(nSubs), np.max(nSubs),linestyles='dashed',label="Expected")

	    # Title
	    plt.title("Coverage (" + str(np.int(100*p)) + "% probability, "  + str(nBoot) + " bootstraps, " + str(nReals) + " realizations)")

	    # Axes
	    plt.xlabel("Number of subjects")
	    plt.ylabel("Observed coverage")

	    # Legend
	    plt.legend()

	    # Save plots
	    plt.savefig(os.path.join(OutDir, 'coverage'+str(np.int(100*p))+'.png'))

	    # Clear figure
	    plt.clf()

	# -----------------------------------------------------------------
	# For sample size, make quantile plots
	# -----------------------------------------------------------------
	# Loop through sample sizes making plots
	for i, nSub in enumerate(nSubs):

		# Plot quantiles for estimated along true boundary
	    #plt.plot(pVals,covTable_true[i,:],color="red",label="True boundary")

	    # Plot quantiles for estimated along estimated boundary
	    #plt.plot(pVals,covTable_est[i,:],color="blue",label="Estimated boundary")

		# Plot quantiles for estimated along true boundary (Interpolated)
	    plt.plot(pVals,covTable_true_intrp[i,:],linestyle='dashed',color="red",label="True boundary (Interpolated)")

	    # Plot quantiles for estimated along estimated boundary (Interpolated)
	    plt.plot(pVals,covTable_est_intrp[i,:],linestyle='dashed',color="blue",label="Estimated boundary (Interpolated)")

		# Plot quantiles for estimated along true boundary (Interpolated)
	    plt.plot(pVals,pVals,color="grey",label="y=x")

	    # Title
	    plt.title("Q-Q (" + str(nSub) + " subjects, "  + str(nBoot) + " bootstraps, " + str(nReals) + " realizations)")

	    # Axes
	    plt.xlabel("Expected coverage")
	    plt.ylabel("Observed coverage")

	    # Legend
	    plt.legend(loc="upper left")

	    # Save plots
	    plt.savefig(os.path.join(OutDir, 'qq'+str(nSub)+'.png'))

	    # Clear figure
	    plt.clf()

# Run for example output.
join_and_plot('/home/tommaullin/Documents/ConfRes/2Sample/v6', np.int32(np.linspace(40,500,24)), 5000, 5000, np.linspace(0,1,21))
