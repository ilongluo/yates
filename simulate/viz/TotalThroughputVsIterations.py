import CommonConf
import CommonViz

import re
from collections import OrderedDict
import numpy as np
import matplotlib.pyplot as pp
import sys

EXPERIMENT_NAME = "TotalThroughputVsIterations"
X_LABEL         = "Iterations"
Y_LABEL         = "Total Throughput"

def main(dirn, fname, solvers):
  (xs, ysPerSolver, ydevsPerSolver) = CommonViz.parseData(dirn, fname, solvers)

  CommonConf.setupMPPDefaults()
  fmts = CommonConf.getLineFormats()
  mrkrs = CommonConf.getLineMarkers()
  fig = pp.figure()
  ax = fig.add_subplot(111)
  # ax.set_xscale("log", basex=2)

  index = 0
  for (solver, ys), (solver, ydevs) in zip(ysPerSolver.iteritems(),ydevsPerSolver.iteritems()) :
    ax.errorbar(xs, ys, yerr=ydevs, label=solver, marker=mrkrs[index], linestyle=fmts[index], alpha=0.8)
    index = index + 1

  ax.set_xlabel(X_LABEL);
  ax.set_ylabel(Y_LABEL);
  ax.legend(loc='best', fancybox=True)

  pp.savefig(dirn+"/"+fname+"-".join(solvers)+".svg")

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print "Usage: " + sys.argv[0] + " RunId" + " [optional (list_of_schemes)]"
  else:
    main("expData/"+sys.argv[1], EXPERIMENT_NAME, set(sys.argv[2:]))