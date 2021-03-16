import os
import numpy as np
import yaml


def generateCfgs(OutDir, simNo):

    # Make simulation directory
    simDir = os.path.join(OutDir, 'sim'+str(simNo))
    if not os.path.exists(simDir):
        os.mkdir(simDir)

    # Make directory to store configuration files
    if not os.path.exists(os.path.join(simDir,'cfgs')):
        os.mkdir(os.path.join(simDir,'cfgs'))


    # ==========================================================================
    # Basic inputs for all simulations
    # ==========================================================================

    # New empty inputs structure
    inputs={}

    # Add output directory
    inputs['OutDir'] = OutDir

    # Add simulation number (helps identify simulation)
    inputs['simNo'] = simNo

    # Add range of p-values
    inputs['p'] = 'np.linspace(0,1,21)'

    # Add tau expression
    inputs['tau'] = '1/np.sqrt(nSub)'

    # Add number of realizations
    inputs['nReals'] = 500

    # Add number of bootstraps
    inputs['nBoot'] = 5000

    # Create mu1 and mu2 specification
    mu1 = {}
    mu2 = {}

    # Create noise1 and noise2 specification
    noise1 = {}
    noise2 = {}

    # These are our sample sizes:
    nSubs = np.linspace(40,500,24)
    fg_nSubs = np.array([100,300,500])  

    # ==========================================================================
    #
    # Simulation 1: Circles moving closer
    #
    # --------------------------------------------------------------------------
    #
    # In this simulation setting, we are interested in moving two circles of 
    # equal diameter close to one another. For this reason, we vary the circles
    # center and, as usual, the number of subjects.
    #
    # ==========================================================================
    if simNo==1:

        # These are our circles centers
        centers = np.arange(-20,32,2)

        # Add threshold c
        inputs['c'] = 2

        # Add mode
        inputs['mode'] = 1

        # Add FWHM for noise
        noise1['FWHM'] = '[0, 3, 3]'

        # Add type for noise 1
        noise1['type'] = 'homogen'

        # Add FWHM  for noise 2
        noise2['FWHM'] = '[0, 3, 3]'

        # Add type for noise 2
        noise2['type'] = 'homogen'

        # Save noises
        inputs['noise1'] = noise1
        inputs['noise2'] = noise2

        # Add mu1 type
        mu1['type'] = 'circle2D' 

        # Add mu1 fwhm
        mu1['fwhm'] = 'np.array([5,5])'

        # Add mu1 radius
        mu1['r'] = 30

        # Add mu1 magnitude
        mu1['mag'] = 3

        # Add mu1 center (we only vary mu2)
        mu1['center'] = 'np.array([-20,0])'

        # Add mu1 to inputs
        inputs['mu1'] = mu1

        # Add mu2 type
        mu2['type'] = 'circle2D' 

        # Add mu2 fwhm
        mu2['fwhm'] = 'np.array([5,5])'

        # Add mu2 radius
        mu2['r'] = 30

        # Add mu2 magnitude
        mu2['mag'] = 3

        # We will generate figures for these settings
        fg_centers = np.array([-20,0,20,28])

        # Id for config file
        cfgId = 1

        # Loop through all center settings
        for center in centers:

            # Add mu2 center
            mu2['center']= 'np.array(['+str(center)+',0])'

            # Add mu2 to inputs
            inputs['mu2'] = mu2

            # Loop through all nSub settings
            for nSub in nSubs:

                # Add nSub to inputs
                inputs['nSub'] = int(nSub)

                # Save cfg ID (handy to have around)
                inputs['cfgId'] = int(cfgId)

                # Record if we want to save figures for this design or not
                if (nSub in fg_nSubs) and (center in fg_centers):

                    # In this case we do want to save  figures
                    inputs['figGen']=1

                else:

                    # In this case we do want to save  figures
                    inputs['figGen']=0

                # Save the yml
                with open(os.path.join(simDir,'cfgs','cfg'+str(cfgId)+'.yml'), 'w') as outfile:
                    yaml.dump(inputs, outfile, default_flow_style=False)

                # Incremement cfgID
                cfgId = cfgId + 1

        # Delete fields which vary across simulation
        del inputs['mu2']['center'], inputs['figGen'], inputs['cfgId'], inputs['nSub']

    # ==========================================================================
    #
    # Simulation 2: Circles moving closer (but lower fwhm)
    #
    # --------------------------------------------------------------------------
    #
    # In this simulation setting, we are interested in moving two circles of 
    # equal diameter close to one another. For this reason, we vary the circles
    # center and, as usual, the number of subjects. This differs from the 
    # previous setting in terms of smoothing and fwhm.
    #
    # ==========================================================================
    if simNo==2:

        # These are our circles centers
        centers = np.arange(-20,32,2)

        # Add threshold c
        inputs['c'] = 2/3

        # Add mode
        inputs['mode'] = 1

        # Add FWHM for noise
        noise1['FWHM'] = '[0, 3, 3]'

        # Add type for noise 1
        noise1['type'] = 'homogen'

        # Add FWHM  for noise 2
        noise2['FWHM'] = '[0, 3, 3]'

        # Add type for noise 2
        noise2['type'] = 'homogen'

        # Save noises
        inputs['noise1'] = noise1
        inputs['noise2'] = noise2

        # Add mu1 type
        mu1['type'] = 'circle2D' 

        # Add mu1 fwhm
        mu1['fwhm'] = 'np.array([5,5])'

        # Add mu1 radius
        mu1['r'] = 30

        # Add mu1 magnitude
        mu1['mag'] = 1

        # Add mu1 center (we only vary mu2)
        mu1['center'] = 'np.array([-20,0])'

        # Add mu1 to inputs
        inputs['mu1'] = mu1

        # Add mu2 type
        mu2['type'] = 'circle2D' 

        # Add mu2 fwhm
        mu2['fwhm'] = 'np.array([5,5])'

        # Add mu2 radius
        mu2['r'] = 30

        # Add mu2 magnitude
        mu2['mag'] = 1

        # We will generate figures for these settings
        fg_centers = np.array([-20,0,20,28])

        # Id for config file
        cfgId = 1

        # Loop through all center settings
        for center in centers:

            # Add mu2 center
            mu2['center']= 'np.array(['+str(center)+',0])'

            # Add mu2 to inputs
            inputs['mu2'] = mu2

            # Loop through all nSub settings
            for nSub in nSubs:

                # Add nSub to inputs
                inputs['nSub'] = int(nSub)

                # Save cfg ID (handy to have around)
                inputs['cfgId'] = int(cfgId)

                # Record if we want to save figures for this design or not
                if (nSub in fg_nSubs) and (center in fg_centers):

                    # In this case we do want to save  figures
                    inputs['figGen']=1

                else:

                    # In this case we do want to save  figures
                    inputs['figGen']=0

                # Save the yml
                with open(os.path.join(simDir,'cfgs','cfg'+str(cfgId)+'.yml'), 'w') as outfile:
                    yaml.dump(inputs, outfile, default_flow_style=False)

                # Incremement cfgID
                cfgId = cfgId + 1

        # Delete fields which vary across simulation
        del inputs['mu2']['center'], inputs['figGen'], inputs['cfgId'], inputs['nSub']


    # ==========================================================================
    #
    # Simulation 3: Squares moving closer
    #
    # --------------------------------------------------------------------------
    #
    # In this simulation setting, we are interested in moving two squares of 
    # equal diameter close to one another. For this reason, we vary the squares
    # center and, as usual, the number of subjects.
    #
    # ==========================================================================
    if simNo==3:

        # These are our circles centers
        centers = np.arange(-20,32,2)

        # Add threshold c
        inputs['c'] = 2

        # Add mode
        inputs['mode'] = 1

        # Add FWHM for noise
        noise1['FWHM'] = '[0, 3, 3]'

        # Add type for noise 1
        noise1['type'] = 'homogen'

        # Add FWHM  for noise 2
        noise2['FWHM'] = '[0, 3, 3]'

        # Add type for noise 2
        noise2['type'] = 'homogen'

        # Save noises
        inputs['noise1'] = noise1
        inputs['noise2'] = noise2

        # Add mu1 type
        mu1['type'] = 'square2D' 

        # Add mu1 fwhm
        mu1['fwhm'] = 'np.array([5,5])'

        # Add mu1 radius
        mu1['r'] = 30

        # Add mu1 magnitude
        mu1['mag'] = 3

        # Add mu1 center (we only vary mu2)
        mu1['center'] = 'np.array([-20,0])'

        # Add mu1 to inputs
        inputs['mu1'] = mu1

        # Add mu2 type
        mu2['type'] = 'square2D' 

        # Add mu2 fwhm
        mu2['fwhm'] = 'np.array([5,5])'

        # Add mu2 radius
        mu2['r'] = 30

        # Add mu2 magnitude
        mu2['mag'] = 3

        # We will generate figures for these settings
        fg_centers = np.array([-20,0,20,28])

        # Id for config file
        cfgId = 1

        # Loop through all center settings
        for center in centers:

            # Add mu2 center
            mu2['center']= 'np.array(['+str(center)+',0])'

            # Add mu2 to inputs
            inputs['mu2'] = mu2

            # Loop through all nSub settings
            for nSub in nSubs:

                # Add nSub to inputs
                inputs['nSub'] = int(nSub)

                # Save cfg ID (handy to have around)
                inputs['cfgId'] = int(cfgId)

                # Record if we want to save figures for this design or not
                if (nSub in fg_nSubs) and (center in fg_centers):

                    # In this case we do want to save  figures
                    inputs['figGen']=1

                else:

                    # In this case we do want to save  figures
                    inputs['figGen']=0

                # Save the yml
                with open(os.path.join(simDir,'cfgs','cfg'+str(cfgId)+'.yml'), 'w') as outfile:
                    yaml.dump(inputs, outfile, default_flow_style=False)

                # Incremement cfgID
                cfgId = cfgId + 1

        # Delete fields which vary across simulation
        del inputs['mu2']['center'], inputs['figGen'], inputs['cfgId'], inputs['nSub']

    # ==========================================================================
    #
    # Simulation 4: Squares moving closer (but lower fwhm)
    #
    # --------------------------------------------------------------------------
    #
    # In this simulation setting, we are interested in moving two squares of 
    # equal diameter close to one another. For this reason, we vary the squares
    # center and, as usual, the number of subjects. This differs from the 
    # previous setting in terms of smoothing and fwhm.
    #
    # ==========================================================================
    if simNo==4:

        # These are our circles centers
        centers = np.arange(-20,32,2)

        # Add threshold c
        inputs['c'] = 2/3

        # Add mode
        inputs['mode'] = 1

        # Add FWHM for noise
        noise1['FWHM'] = '[0, 3, 3]'

        # Add type for noise 1
        noise1['type'] = 'homogen'

        # Add FWHM  for noise 2
        noise2['FWHM'] = '[0, 3, 3]'

        # Add type for noise 2
        noise2['type'] = 'homogen'

        # Save noises
        inputs['noise1'] = noise1
        inputs['noise2'] = noise2

        # Add mu1 type
        mu1['type'] = 'square2D' 

        # Add mu1 fwhm
        mu1['fwhm'] = 'np.array([5,5])'

        # Add mu1 radius
        mu1['r'] = 30

        # Add mu1 magnitude
        mu1['mag'] = 1

        # Add mu1 center (we only vary mu2)
        mu1['center'] = 'np.array([-20,0])'

        # Add mu1 to inputs
        inputs['mu1'] = mu1

        # Add mu2 type
        mu2['type'] = 'square2D' 

        # Add mu2 fwhm
        mu2['fwhm'] = 'np.array([5,5])'

        # Add mu2 radius
        mu2['r'] = 30

        # Add mu2 magnitude
        mu2['mag'] = 1

        # We will generate figures for these settings
        fg_centers = np.array([-20,0,20,28])

        # Id for config file
        cfgId = 1

        # Loop through all center settings
        for center in centers:

            # Add mu2 center
            mu2['center']= 'np.array(['+str(center)+',0])'

            # Add mu2 to inputs
            inputs['mu2'] = mu2

            # Loop through all nSub settings
            for nSub in nSubs:

                # Add nSub to inputs
                inputs['nSub'] = int(nSub)

                # Save cfg ID (handy to have around)
                inputs['cfgId'] = int(cfgId)

                # Record if we want to save figures for this design or not
                if (nSub in fg_nSubs) and (center in fg_centers):

                    # In this case we do want to save  figures
                    inputs['figGen']=1

                else:

                    # In this case we do want to save  figures
                    inputs['figGen']=0

                # Save the yml
                with open(os.path.join(simDir,'cfgs','cfg'+str(cfgId)+'.yml'), 'w') as outfile:
                    yaml.dump(inputs, outfile, default_flow_style=False)

                # Incremement cfgID
                cfgId = cfgId + 1

        # Delete fields which vary across simulation
        del inputs['mu2']['center'], inputs['figGen'], inputs['cfgId'], inputs['nSub']

    # ==========================================================================
    #
    # Simulation 5: Squares moving closer (mode 2)
    #
    # --------------------------------------------------------------------------
    #
    # In this simulation setting, we are interested in moving two squares of 
    # equal diameter close to one another. For this reason, we vary the squares
    # center and, as usual, the number of subjects.
    #
    # ==========================================================================
    if simNo==5:

        # These are our circles centers
        centers = np.arange(-20,32,2)

        # Add threshold c
        inputs['c'] = 2

        # Add mode
        inputs['mode'] = 2

        # Add FWHM for noise
        noise1['FWHM'] = '[0, 3, 3]'

        # Add type for noise 1
        noise1['type'] = 'homogen'

        # Add FWHM  for noise 2
        noise2['FWHM'] = '[0, 3, 3]'

        # Add type for noise 2
        noise2['type'] = 'homogen'

        # Save noises
        inputs['noise1'] = noise1
        inputs['noise2'] = noise2

        # Add mu1 type
        mu1['type'] = 'square2D' 

        # Add mu1 fwhm
        mu1['fwhm'] = 'np.array([5,5])'

        # Add mu1 radius
        mu1['r'] = 30

        # Add mu1 magnitude
        mu1['mag'] = 3

        # Add mu1 center (we only vary mu2)
        mu1['center'] = 'np.array([-20,0])'

        # Add mu1 to inputs
        inputs['mu1'] = mu1

        # Add mu2 type
        mu2['type'] = 'square2D' 

        # Add mu2 fwhm
        mu2['fwhm'] = 'np.array([5,5])'

        # Add mu2 radius
        mu2['r'] = 30

        # Add mu2 magnitude
        mu2['mag'] = 3

        # We will generate figures for these settings
        fg_centers = np.array([-20,0,20,28])

        # Id for config file
        cfgId = 1

        # Loop through all center settings
        for center in centers:

            # Add mu2 center
            mu2['center']= 'np.array(['+str(center)+',0])'

            # Add mu2 to inputs
            inputs['mu2'] = mu2

            # Loop through all nSub settings
            for nSub in nSubs:

                # Add nSub to inputs
                inputs['nSub'] = int(nSub)

                # Save cfg ID (handy to have around)
                inputs['cfgId'] = int(cfgId)

                # Record if we want to save figures for this design or not
                if (nSub in fg_nSubs) and (center in fg_centers):

                    # In this case we do want to save  figures
                    inputs['figGen']=1

                else:

                    # In this case we do want to save  figures
                    inputs['figGen']=0

                # Save the yml
                with open(os.path.join(simDir,'cfgs','cfg'+str(cfgId)+'.yml'), 'w') as outfile:
                    yaml.dump(inputs, outfile, default_flow_style=False)

                # Incremement cfgID
                cfgId = cfgId + 1

        # Delete fields which vary across simulation
        del inputs['mu2']['center'], inputs['figGen'], inputs['cfgId'], inputs['nSub']

    # ==========================================================================
    #
    # Simulation 6: Squares moving closer (but lower fwhm) (mode 2)
    #
    # --------------------------------------------------------------------------
    #
    # In this simulation setting, we are interested in moving two squares of 
    # equal diameter close to one another. For this reason, we vary the squares
    # center and, as usual, the number of subjects. This differs from the 
    # previous setting in terms of smoothing and fwhm.
    #
    # ==========================================================================
    if simNo==6:

        # These are our circles centers
        centers = np.arange(-20,32,2)

        # Add threshold c
        inputs['c'] = 2/3

        # Add mode
        inputs['mode'] = 2

        # Add FWHM for noise
        noise1['FWHM'] = '[0, 3, 3]'

        # Add type for noise 1
        noise1['type'] = 'homogen'

        # Add FWHM  for noise 2
        noise2['FWHM'] = '[0, 3, 3]'

        # Add type for noise 2
        noise2['type'] = 'homogen'

        # Save noises
        inputs['noise1'] = noise1
        inputs['noise2'] = noise2

        # Add mu1 type
        mu1['type'] = 'square2D' 

        # Add mu1 fwhm
        mu1['fwhm'] = 'np.array([5,5])'

        # Add mu1 radius
        mu1['r'] = 30

        # Add mu1 magnitude
        mu1['mag'] = 1

        # Add mu1 center (we only vary mu2)
        mu1['center'] = 'np.array([-20,0])'

        # Add mu1 to inputs
        inputs['mu1'] = mu1

        # Add mu2 type
        mu2['type'] = 'square2D' 

        # Add mu2 fwhm
        mu2['fwhm'] = 'np.array([5,5])'

        # Add mu2 radius
        mu2['r'] = 30

        # Add mu2 magnitude
        mu2['mag'] = 1

        # We will generate figures for these settings
        fg_centers = np.array([-20,0,20,28])

        # Id for config file
        cfgId = 1

        # Loop through all center settings
        for center in centers:

            # Add mu2 center
            mu2['center']= 'np.array(['+str(center)+',0])'

            # Add mu2 to inputs
            inputs['mu2'] = mu2

            # Loop through all nSub settings
            for nSub in nSubs:

                # Add nSub to inputs
                inputs['nSub'] = int(nSub)

                # Save cfg ID (handy to have around)
                inputs['cfgId'] = int(cfgId)

                # Record if we want to save figures for this design or not
                if (nSub in fg_nSubs) and (center in fg_centers):

                    # In this case we do want to save  figures
                    inputs['figGen']=1

                else:

                    # In this case we do want to save  figures
                    inputs['figGen']=0

                # Save the yml
                with open(os.path.join(simDir,'cfgs','cfg'+str(cfgId)+'.yml'), 'w') as outfile:
                    yaml.dump(inputs, outfile, default_flow_style=False)

                # Incremement cfgID
                cfgId = cfgId + 1

        # Delete fields which vary across simulation
        del inputs['mu2']['center'], inputs['figGen'], inputs['cfgId'], inputs['nSub']


    # ==========================================================================
    #
    # Simulation 7: Squares moving closer (mode 3)
    #
    # --------------------------------------------------------------------------
    #
    # In this simulation setting, we are interested in moving two squares of 
    # equal diameter close to one another. For this reason, we vary the squares
    # center and, as usual, the number of subjects.
    #
    # ==========================================================================
    if simNo==7:

        # These are our circles centers
        centers = np.arange(-20,32,2)

        # Add threshold c
        inputs['c'] = 2

        # Add mode
        inputs['mode'] = 3

        # Add FWHM for noise
        noise1['FWHM'] = '[0, 3, 3]'

        # Add type for noise 1
        noise1['type'] = 'homogen'

        # Add FWHM  for noise 2
        noise2['FWHM'] = '[0, 3, 3]'

        # Add type for noise 2
        noise2['type'] = 'homogen'

        # Save noises
        inputs['noise1'] = noise1
        inputs['noise2'] = noise2

        # Add mu1 type
        mu1['type'] = 'square2D' 

        # Add mu1 fwhm
        mu1['fwhm'] = 'np.array([5,5])'

        # Add mu1 radius
        mu1['r'] = 30

        # Add mu1 magnitude
        mu1['mag'] = 3

        # Add mu1 center (we only vary mu2)
        mu1['center'] = 'np.array([-20,0])'

        # Add mu1 to inputs
        inputs['mu1'] = mu1

        # Add mu2 type
        mu2['type'] = 'square2D' 

        # Add mu2 fwhm
        mu2['fwhm'] = 'np.array([5,5])'

        # Add mu2 radius
        mu2['r'] = 30

        # Add mu2 magnitude
        mu2['mag'] = 3

        # We will generate figures for these settings
        fg_centers = np.array([-20,0,20,28])

        # Id for config file
        cfgId = 1

        # Loop through all center settings
        for center in centers:

            # Add mu2 center
            mu2['center']= 'np.array(['+str(center)+',0])'

            # Add mu2 to inputs
            inputs['mu2'] = mu2

            # Loop through all nSub settings
            for nSub in nSubs:

                # Add nSub to inputs
                inputs['nSub'] = int(nSub)

                # Save cfg ID (handy to have around)
                inputs['cfgId'] = int(cfgId)

                # Record if we want to save figures for this design or not
                if (nSub in fg_nSubs) and (center in fg_centers):

                    # In this case we do want to save  figures
                    inputs['figGen']=1

                else:

                    # In this case we do want to save  figures
                    inputs['figGen']=0

                # Save the yml
                with open(os.path.join(simDir,'cfgs','cfg'+str(cfgId)+'.yml'), 'w') as outfile:
                    yaml.dump(inputs, outfile, default_flow_style=False)

                # Incremement cfgID
                cfgId = cfgId + 1

        # Delete fields which vary across simulation
        del inputs['mu2']['center'], inputs['figGen'], inputs['cfgId'], inputs['nSub']

    # ==========================================================================
    #
    # Simulation 8: Squares moving closer (but lower fwhm) (mode 3)
    #
    # --------------------------------------------------------------------------
    #
    # In this simulation setting, we are interested in moving two squares of 
    # equal diameter close to one another. For this reason, we vary the squares
    # center and, as usual, the number of subjects. This differs from the 
    # previous setting in terms of smoothing and fwhm.
    #
    # ==========================================================================
    if simNo==8:

        # These are our circles centers
        centers = np.arange(-20,32,2)

        # Add threshold c
        inputs['c'] = 2/3

        # Add mode
        inputs['mode'] = 3

        # Add FWHM for noise
        noise1['FWHM'] = '[0, 3, 3]'

        # Add type for noise 1
        noise1['type'] = 'homogen'

        # Add FWHM  for noise 2
        noise2['FWHM'] = '[0, 3, 3]'

        # Add type for noise 2
        noise2['type'] = 'homogen'

        # Save noises
        inputs['noise1'] = noise1
        inputs['noise2'] = noise2

        # Add mu1 type
        mu1['type'] = 'square2D' 

        # Add mu1 fwhm
        mu1['fwhm'] = 'np.array([5,5])'

        # Add mu1 radius
        mu1['r'] = 30

        # Add mu1 magnitude
        mu1['mag'] = 1

        # Add mu1 center (we only vary mu2)
        mu1['center'] = 'np.array([-20,0])'

        # Add mu1 to inputs
        inputs['mu1'] = mu1

        # Add mu2 type
        mu2['type'] = 'square2D' 

        # Add mu2 fwhm
        mu2['fwhm'] = 'np.array([5,5])'

        # Add mu2 radius
        mu2['r'] = 30

        # Add mu2 magnitude
        mu2['mag'] = 1

        # We will generate figures for these settings
        fg_centers = np.array([-20,0,20,28])

        # Id for config file
        cfgId = 1

        # Loop through all center settings
        for center in centers:

            # Add mu2 center
            mu2['center']= 'np.array(['+str(center)+',0])'

            # Add mu2 to inputs
            inputs['mu2'] = mu2

            # Loop through all nSub settings
            for nSub in nSubs:

                # Add nSub to inputs
                inputs['nSub'] = int(nSub)

                # Save cfg ID (handy to have around)
                inputs['cfgId'] = int(cfgId)

                # Record if we want to save figures for this design or not
                if (nSub in fg_nSubs) and (center in fg_centers):

                    # In this case we do want to save  figures
                    inputs['figGen']=1

                else:

                    # In this case we do want to save  figures
                    inputs['figGen']=0

                # Save the yml
                with open(os.path.join(simDir,'cfgs','cfg'+str(cfgId)+'.yml'), 'w') as outfile:
                    yaml.dump(inputs, outfile, default_flow_style=False)

                # Incremement cfgID
                cfgId = cfgId + 1

        # Delete fields which vary across simulation
        del inputs['mu2']['center'], inputs['figGen'], inputs['cfgId'], inputs['nSub']

    # ==========================================================================
    #
    # Simulation 9: Changing noise fwhm in one square (mode 3, high mu fwhm)
    #
    # --------------------------------------------------------------------------
    #
    # In this simulation setting, we are interested in changing the fwhm of the
    # noise in one of our fields but keeping the other constant (i.e. to see
    # if having different spatial correlations between the fields has an affect.
    # As always it is run across a range of subjects as well
    #
    # ==========================================================================
    if simNo==9:

        # These are our noise fwhms
        FWHM2s = np.linspace(1,6,26)

        # Add threshold c
        inputs['c'] = 2

        # Add mode
        inputs['mode'] = 3

        # Add FWHM for noise 1
        noise1['FWHM'] = '[0, 3, 3]'

        # Add type for noise 1
        noise1['type'] = 'homogen'

        # Add type for noise 2
        noise2['type'] = 'homogen'

        # Save noise 1
        inputs['noise1'] = noise1

        # Add mu1 type
        mu1['type'] = 'square2D' 

        # Add mu1 fwhm
        mu1['fwhm'] = 'np.array([5,5])'

        # Add mu1 radius
        mu1['r'] = 30

        # Add mu1 magnitude
        mu1['mag'] = 3

        # Add mu1 center
        mu1['center'] = 'np.array([-20,0])'

        # Add mu1 to inputs
        inputs['mu1'] = mu1

        # Add mu2 type
        mu2['type'] = 'square2D' 

        # Add mu2 fwhm
        mu2['fwhm'] = 'np.array([5,5])'

        # Add mu2 radius
        mu2['r'] = 30

        # Add mu2 magnitude
        mu2['mag'] = 3

        # Add mu2 center
        mu2['center'] = 'np.array([0,0])'

        # Add mu2 to inputs
        inputs['mu2'] = mu2

        # We will generate figures for these settings
        fg_FWHM2s = np.array([1,3,6])

        # Id for config file
        cfgId = 1

        # Loop through all FWHM2 settings
        for FWHM2 in FWHM2s:

            # Add FWHM for second noise field
            noise2['FWHM'] = '[0, ' + str(FWHM2) + ', ' + str(FWHM2) + ']'

            # Save noise field 2
            inputs['noise2'] = noise2   

            # Loop through all nSub settings
            for nSub in nSubs:

                # Add nSub to inputs
                inputs['nSub'] = int(nSub)

                # Save cfg ID (handy to have around)
                inputs['cfgId'] = int(cfgId)

                # Record if we want to save figures for this design or not
                if (nSub in fg_nSubs) and (FWHM2 in fg_FWHM2s):

                    # In this case we do want to save  figures
                    inputs['figGen']=1

                else:

                    # In this case we do want to save  figures
                    inputs['figGen']=0

                # Save the yml
                with open(os.path.join(simDir,'cfgs','cfg'+str(cfgId)+'.yml'), 'w') as outfile:
                    yaml.dump(inputs, outfile, default_flow_style=False)

                # Incremement cfgID
                cfgId = cfgId + 1

        # Delete fields which vary across simulation
        del inputs['noise2']['FWHM'], inputs['figGen'], inputs['cfgId'], inputs['nSub']

    # ==========================================================================
    #
    # Simulation 10: Changing noise fwhm in one square (mode 3, low mu fwhm)
    #
    # --------------------------------------------------------------------------
    #
    # In this simulation setting, we are interested in changing the fwhm of the
    # noise in one of our fields but keeping the other constant (i.e. to see
    # if having different spatial correlations between the fields has an affect.
    # As always it is run across a range of subjects as well
    #
    # ==========================================================================
    if simNo==10:

        # These are our noise fwhms
        FWHM2s = np.linspace(1,6,26)

        # Add threshold c
        inputs['c'] = 2/3

        # Add mode
        inputs['mode'] = 3

        # Add FWHM for noise 1
        noise1['FWHM'] = '[0, 3, 3]'

        # Add type for noise 1
        noise1['type'] = 'homogen'

        # Add type for noise 2
        noise2['type'] = 'homogen'

        # Save noises
        inputs['noise1'] = noise1

        # Add mu1 type
        mu1['type'] = 'square2D' 

        # Add mu1 fwhm
        mu1['fwhm'] = 'np.array([5,5])'

        # Add mu1 radius
        mu1['r'] = 30

        # Add mu1 magnitude
        mu1['mag'] = 1

        # Add mu1 center
        mu1['center'] = 'np.array([-20,0])'

        # Add mu1 to inputs
        inputs['mu1'] = mu1

        # Add mu2 type
        mu2['type'] = 'square2D' 

        # Add mu2 fwhm
        mu2['fwhm'] = 'np.array([5,5])'

        # Add mu2 radius
        mu2['r'] = 30

        # Add mu2 magnitude
        mu2['mag'] = 1

        # Add mu2 center
        mu2['center'] = 'np.array([0,0])'

        # Add mu2 to inputs
        inputs['mu2'] = mu2

        # We will generate figures for these settings
        fg_FWHM2s = np.array([1,3,6])

        # Id for config file
        cfgId = 1

        # Loop through all FWHM2 settings
        for FWHM2 in FWHM2s:

            # Add FWHM  for noise 2
            noise2['FWHM'] = '[0, ' + str(FWHM2) + ', ' + str(FWHM2) + ']'

            # Add noise 2 to inputs
            inputs['noise2'] = noise2

            # Loop through all nSub settings
            for nSub in nSubs:

                # Add nSub to inputs
                inputs['nSub'] = int(nSub)

                # Save cfg ID (handy to have around)
                inputs['cfgId'] = int(cfgId)

                # Record if we want to save figures for this design or not
                if (nSub in fg_nSubs) and (FWHM2 in fg_FWHM2s):

                    # In this case we do want to save  figures
                    inputs['figGen']=1

                else:

                    # In this case we do want to save  figures
                    inputs['figGen']=0

                # Save the yml
                with open(os.path.join(simDir,'cfgs','cfg'+str(cfgId)+'.yml'), 'w') as outfile:
                    yaml.dump(inputs, outfile, default_flow_style=False)

                # Incremement cfgID
                cfgId = cfgId + 1

        # Delete fields which vary across simulation
        del inputs['noise2']['FWHM'], inputs['figGen'], inputs['cfgId'], inputs['nSub']


    # ==========================================================================
    #
    # Simulation 11: Squares moving closer (mode 3) (but heterogenous ramp on
    # one square)
    #
    # --------------------------------------------------------------------------
    #
    # In this simulation setting, we are interested in moving two squares of 
    # equal diameter close to one another. For this reason, we vary the squares
    # center and, as usual, the number of subjects.
    #
    # ==========================================================================
    if simNo==11:

        # These are our circles centers
        centers = np.arange(-20,32,2)

        # Add threshold c
        inputs['c'] = 2

        # Add mode
        inputs['mode'] = 3

        # Add FWHM for noise
        noise1['FWHM'] = '[0, 3, 3]'

        # Add type for noise 1
        noise1['type'] = 'homogen'

        # Add FWHM  for noise 2
        noise2['FWHM'] = '[0, 3, 3]'

        # Add type for noise 2
        noise2['type'] = 'heterogen'

        # Save noises
        inputs['noise1'] = noise1
        inputs['noise2'] = noise2

        # Add mu1 type
        mu1['type'] = 'square2D' 

        # Add mu1 fwhm
        mu1['fwhm'] = 'np.array([5,5])'

        # Add mu1 radius
        mu1['r'] = 30

        # Add mu1 magnitude
        mu1['mag'] = 3

        # Add mu1 center (we only vary mu2)
        mu1['center'] = 'np.array([-20,0])'

        # Add mu1 to inputs
        inputs['mu1'] = mu1

        # Add mu2 type
        mu2['type'] = 'square2D' 

        # Add mu2 fwhm
        mu2['fwhm'] = 'np.array([5,5])'

        # Add mu2 radius
        mu2['r'] = 30

        # Add mu2 magnitude
        mu2['mag'] = 3

        # We will generate figures for these settings
        fg_centers = np.array([-20,0,20,28])

        # Id for config file
        cfgId = 1

        # Loop through all center settings
        for center in centers:

            # Add mu2 center
            mu2['center']= 'np.array(['+str(center)+',0])'

            # Add mu2 to inputs
            inputs['mu2'] = mu2

            # Loop through all nSub settings
            for nSub in nSubs:

                # Add nSub to inputs
                inputs['nSub'] = int(nSub)

                # Save cfg ID (handy to have around)
                inputs['cfgId'] = int(cfgId)

                # Record if we want to save figures for this design or not
                if (nSub in fg_nSubs) and (center in fg_centers):

                    # In this case we do want to save  figures
                    inputs['figGen']=1

                else:

                    # In this case we do want to save  figures
                    inputs['figGen']=0

                # Save the yml
                with open(os.path.join(simDir,'cfgs','cfg'+str(cfgId)+'.yml'), 'w') as outfile:
                    yaml.dump(inputs, outfile, default_flow_style=False)

                # Incremement cfgID
                cfgId = cfgId + 1

        # Delete fields which vary across simulation
        del inputs['mu2']['center'], inputs['figGen'], inputs['cfgId'], inputs['nSub']

    # ==========================================================================
    #
    # Simulation 12: Squares moving closer (but lower fwhm) (mode 3)  (but 
    # heterogenous ramp on one square)
    #
    # --------------------------------------------------------------------------
    #
    # In this simulation setting, we are interested in moving two squares of 
    # equal diameter close to one another. For this reason, we vary the squares
    # center and, as usual, the number of subjects. This differs from the 
    # previous setting in terms of smoothing and fwhm.
    #
    # ==========================================================================
    if simNo==12:

        # These are our circles centers
        centers = np.arange(-20,32,2)

        # Add threshold c
        inputs['c'] = 2/3

        # Add mode
        inputs['mode'] = 3

        # Add FWHM for noise
        noise1['FWHM'] = '[0, 3, 3]'

        # Add type for noise 1
        noise1['type'] = 'homogen'

        # Add FWHM  for noise 2
        noise2['FWHM'] = '[0, 3, 3]'

        # Add type for noise 2
        noise2['type'] = 'heterogen'

        # Save noises
        inputs['noise1'] = noise1
        inputs['noise2'] = noise2

        # Add mu1 type
        mu1['type'] = 'square2D' 

        # Add mu1 fwhm
        mu1['fwhm'] = 'np.array([5,5])'

        # Add mu1 radius
        mu1['r'] = 30

        # Add mu1 magnitude
        mu1['mag'] = 1

        # Add mu1 center (we only vary mu2)
        mu1['center'] = 'np.array([-20,0])'

        # Add mu1 to inputs
        inputs['mu1'] = mu1

        # Add mu2 type
        mu2['type'] = 'square2D' 

        # Add mu2 fwhm
        mu2['fwhm'] = 'np.array([5,5])'

        # Add mu2 radius
        mu2['r'] = 30

        # Add mu2 magnitude
        mu2['mag'] = 1

        # We will generate figures for these settings
        fg_centers = np.array([-20,0,20,28])

        # Id for config file
        cfgId = 1

        # Loop through all center settings
        for center in centers:

            # Add mu2 center
            mu2['center']= 'np.array(['+str(center)+',0])'

            # Add mu2 to inputs
            inputs['mu2'] = mu2

            # Loop through all nSub settings
            for nSub in nSubs:

                # Add nSub to inputs
                inputs['nSub'] = int(nSub)

                # Save cfg ID (handy to have around)
                inputs['cfgId'] = int(cfgId)

                # Record if we want to save figures for this design or not
                if (nSub in fg_nSubs) and (center in fg_centers):

                    # In this case we do want to save  figures
                    inputs['figGen']=1

                else:

                    # In this case we do want to save  figures
                    inputs['figGen']=0

                # Save the yml
                with open(os.path.join(simDir,'cfgs','cfg'+str(cfgId)+'.yml'), 'w') as outfile:
                    yaml.dump(inputs, outfile, default_flow_style=False)

                # Incremement cfgID
                cfgId = cfgId + 1

        # Delete fields which vary across simulation
        del inputs['mu2']['center'], inputs['figGen'], inputs['cfgId'], inputs['nSub']


    # ==========================================================================
    #
    # Simulation 13: Squares moving closer (mode 3) (but heterogenous ramp on
    # both squares)
    #
    # --------------------------------------------------------------------------
    #
    # In this simulation setting, we are interested in moving two squares of 
    # equal diameter close to one another. For this reason, we vary the squares
    # center and, as usual, the number of subjects.
    #
    # ==========================================================================
    if simNo==13:

        # These are our circles centers
        centers = np.arange(-20,32,2)

        # Add threshold c
        inputs['c'] = 2

        # Add mode
        inputs['mode'] = 3

        # Add FWHM for noise
        noise1['FWHM'] = '[0, 3, 3]'

        # Add type for noise 1
        noise1['type'] = 'heterogen'

        # Add FWHM  for noise 2
        noise2['FWHM'] = '[0, 3, 3]'

        # Add type for noise 2
        noise2['type'] = 'heterogen'

        # Save noises
        inputs['noise1'] = noise1
        inputs['noise2'] = noise2

        # Add mu1 type
        mu1['type'] = 'square2D' 

        # Add mu1 fwhm
        mu1['fwhm'] = 'np.array([5,5])'

        # Add mu1 radius
        mu1['r'] = 30

        # Add mu1 magnitude
        mu1['mag'] = 3

        # Add mu1 center (we only vary mu2)
        mu1['center'] = 'np.array([-20,0])'

        # Add mu1 to inputs
        inputs['mu1'] = mu1

        # Add mu2 type
        mu2['type'] = 'square2D' 

        # Add mu2 fwhm
        mu2['fwhm'] = 'np.array([5,5])'

        # Add mu2 radius
        mu2['r'] = 30

        # Add mu2 magnitude
        mu2['mag'] = 3

        # We will generate figures for these settings
        fg_centers = np.array([-20,0,20,28])

        # Id for config file
        cfgId = 1

        # Loop through all center settings
        for center in centers:

            # Add mu2 center
            mu2['center']= 'np.array(['+str(center)+',0])'

            # Add mu2 to inputs
            inputs['mu2'] = mu2

            # Loop through all nSub settings
            for nSub in nSubs:

                # Add nSub to inputs
                inputs['nSub'] = int(nSub)

                # Save cfg ID (handy to have around)
                inputs['cfgId'] = int(cfgId)

                # Record if we want to save figures for this design or not
                if (nSub in fg_nSubs) and (center in fg_centers):

                    # In this case we do want to save  figures
                    inputs['figGen']=1

                else:

                    # In this case we do want to save  figures
                    inputs['figGen']=0

                # Save the yml
                with open(os.path.join(simDir,'cfgs','cfg'+str(cfgId)+'.yml'), 'w') as outfile:
                    yaml.dump(inputs, outfile, default_flow_style=False)

                # Incremement cfgID
                cfgId = cfgId + 1

        # Delete fields which vary across simulation
        del inputs['mu2']['center'], inputs['figGen'], inputs['cfgId'], inputs['nSub']

    # ==========================================================================
    #
    # Simulation 14: Squares moving closer (but lower fwhm) (mode 3)  (but 
    # heterogenous ramp on both square)
    #
    # --------------------------------------------------------------------------
    #
    # In this simulation setting, we are interested in moving two squares of 
    # equal diameter close to one another. For this reason, we vary the squares
    # center and, as usual, the number of subjects. This differs from the 
    # previous setting in terms of smoothing and fwhm.
    #
    # ==========================================================================
    if simNo==14:

        # These are our circles centers
        centers = np.arange(-20,32,2)

        # Add threshold c
        inputs['c'] = 2/3

        # Add mode
        inputs['mode'] = 3

        # Add FWHM for noise
        noise1['FWHM'] = '[0, 3, 3]'

        # Add type for noise 1
        noise1['type'] = 'heterogen'

        # Add FWHM  for noise 2
        noise2['FWHM'] = '[0, 3, 3]'

        # Add type for noise 2
        noise2['type'] = 'heterogen'

        # Save noises
        inputs['noise1'] = noise1
        inputs['noise2'] = noise2

        # Add mu1 type
        mu1['type'] = 'square2D' 

        # Add mu1 fwhm
        mu1['fwhm'] = 'np.array([5,5])'

        # Add mu1 radius
        mu1['r'] = 30

        # Add mu1 magnitude
        mu1['mag'] = 1

        # Add mu1 center (we only vary mu2)
        mu1['center'] = 'np.array([-20,0])'

        # Add mu1 to inputs
        inputs['mu1'] = mu1

        # Add mu2 type
        mu2['type'] = 'square2D' 

        # Add mu2 fwhm
        mu2['fwhm'] = 'np.array([5,5])'

        # Add mu2 radius
        mu2['r'] = 30

        # Add mu2 magnitude
        mu2['mag'] = 1

        # We will generate figures for these settings
        fg_centers = np.array([-20,0,20,28])

        # Id for config file
        cfgId = 1

        # Loop through all center settings
        for center in centers:

            # Add mu2 center
            mu2['center']= 'np.array(['+str(center)+',0])'

            # Add mu2 to inputs
            inputs['mu2'] = mu2

            # Loop through all nSub settings
            for nSub in nSubs:

                # Add nSub to inputs
                inputs['nSub'] = int(nSub)

                # Save cfg ID (handy to have around)
                inputs['cfgId'] = int(cfgId)

                # Record if we want to save figures for this design or not
                if (nSub in fg_nSubs) and (center in fg_centers):

                    # In this case we do want to save  figures
                    inputs['figGen']=1

                else:

                    # In this case we do want to save  figures
                    inputs['figGen']=0

                # Save the yml
                with open(os.path.join(simDir,'cfgs','cfg'+str(cfgId)+'.yml'), 'w') as outfile:
                    yaml.dump(inputs, outfile, default_flow_style=False)

                # Incremement cfgID
                cfgId = cfgId + 1

        # Delete fields which vary across simulation
        del inputs['mu2']['center'], inputs['figGen'], inputs['cfgId'], inputs['nSub']


    #--------------------------------------------------------------------------------------
    # Save the baseline configuration (Note: This must be the last file output as the bash
    # script used for running simulations on the cluster will take this files existence as
    # a sign to run the next stage of the simulations)
    #--------------------------------------------------------------------------------------
    # Save the yml
    with open(os.path.join(simDir,'cfgs','baseline_cfg.yml'), 'w') as outfile:
        yaml.dump(inputs, outfile, default_flow_style=False)



#generateCfgs('/home/tommaullin/Documents/ConfRes/tmp/sim7', 7)
