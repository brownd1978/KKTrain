# Ed Callaghan
# Exmaple plot using awkward behaviors
# March 2025

import awkward as ak
import behaviors
from matplotlib import pyplot as plt
import uproot

path = '/home/online1/ejc/public/brownd/dts.mu2e.CeEndpoint.MDC2020r.001210_00000000.art.digi.art.ntuple.root'
with uproot.open(path) as f:
    tree = f['EventNtuple']['ntuple']
    segs = tree['trksegs'].array(library='ak')
    pdgs = tree['trk.pdg'].array(library='ak')

    # sanity check that branches are aligned
    assert(len(segs) == len(pdgs))
    assert(ak.all(ak.num(segs) == ak.num(pdgs)))

    # select on electron fits
    mask = (pdgs == 11)
    segs = segs[mask]

    # select samples at middle of traacker
    mask = segs.sid == 1
    segs = segs[mask]

    # total momentum at sample
    momentum = segs.mom.magnitude()

    # flatten
    momentum = ak.ravel(momentum)

fig = plt.figure()
plt.yscale('log')
plt.xlabel('Momentum [MeV]')
plt.ylabel('Counts')
plt.hist(momentum, bins=100, range=(80.0,110.0), histtype='step')
plt.show()
