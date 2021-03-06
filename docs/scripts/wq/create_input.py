import numpy as np
import xarray as xr

import imod


# Discretization
nrow = 40  # number of rows
ncol = 40  # number of columns
nlay = 15  # number of layers

dz = 10
dx = 250
dy = -dx

x = np.arange(0.5 * dx, dx * ncol, dx)
y = np.arange(-dy * ncol, 0.5 * -dy, dy)

# setup ibound
bnd = xr.DataArray(
    data=np.full((nlay, nrow, ncol), 1.0),
    coords={
        "y": y,
        "x": x,
        "layer": np.arange(1, 1 + nlay),
        "dx": dx,
        "dy": dy,
    },
    dims=("layer", "y", "x"),
)

# set constant heads
bnd[0, :, 0:12] = -1
bnd[0, :, 28:40] = -1

# set up tops and bottoms
top1D = xr.DataArray(
    np.arange(nlay * dz, 0.0, -dz), {"layer": np.arange(1, nlay + 1)}, ("layer")
)

top3D = top1D * xr.full_like(bnd, 1.0)
bot = top3D - dz

# Defining the starting concentrations
sconc = xr.DataArray(
    data=np.full((nlay, nrow, ncol), 35.0),
    coords={
        "y": y,
        "x": x,
        "layer": np.arange(1, nlay + 1),
        "dx": dx,
        "dy": dy,
    },
    dims=("layer", "y", "x"),
)

sconc[0, :, 13:27] = 0.0

# Defining the recharge rates
rch_rate = xr.DataArray(
    data=np.full((nrow, ncol), 0.0),
    coords={"y": y, "x": x, "dx": dx, "dy": dy},
    dims=("y", "x"),
)
rch_rate[:, 13:27] = 0.001

rch_conc = xr.full_like(rch_rate, fill_value=0.0)


# Finally, we build the model.

m = imod.wq.SeawatModel("FreshwaterLens")
m["bas"] = imod.wq.BasicFlow(
    ibound=bnd, top=top3D.sel(layer=1), bottom=bot, starting_head=0.0
)
m["lpf"] = imod.wq.LayerPropertyFlow(
    k_horizontal=10.0, k_vertical=20.0, specific_storage=0.0
)
m["btn"] = imod.wq.BasicTransport(
    icbund=bnd, starting_concentration=sconc, porosity=0.35
)
m["adv"] = imod.wq.AdvectionTVD(courant=1.0)
m["dsp"] = imod.wq.Dispersion(longitudinal=0.0, diffusion_coefficient=0.0)
m["vdf"] = imod.wq.VariableDensityFlow(density_concentration_slope=0.71)
m["rch"] = imod.wq.RechargeHighestActive(rate=rch_rate, concentration=0.0)
m["pcg"] = imod.wq.PreconditionedConjugateGradientSolver(
    max_iter=150, inner_iter=30, hclose=0.0001, rclose=0.1, relax=0.98, damp=1.0
)
m["gcg"] = imod.wq.GeneralizedConjugateGradientSolver(
    max_iter=150,
    inner_iter=30,
    cclose=1.0e-6,
    preconditioner="mic",
    lump_dispersion=True,
)
m["oc"] = imod.wq.OutputControl(save_head_idf=True, save_concentration_idf=True)
m.time_discretization(times=["1900-01-01T00:00", "2000-01-01T00:00"])

# Now we write the model, including runfile:
m.write("FreshwaterLens")
# You can run the model using the command prompt and the iMOD-WQ executable
